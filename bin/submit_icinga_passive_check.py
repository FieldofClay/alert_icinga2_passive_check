import sys, requests, json, re, urllib3, os
import logging, logging.handlers
import splunk

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def setup_logging():
    logger = logging.getLogger('splunk.icinga')    
    SPLUNK_HOME = os.environ['SPLUNK_HOME']
    
    LOGGING_DEFAULT_CONFIG_FILE = os.path.join(SPLUNK_HOME, 'etc', 'log.cfg')
    LOGGING_LOCAL_CONFIG_FILE = os.path.join(SPLUNK_HOME, 'etc', 'log-local.cfg')
    LOGGING_STANZA_NAME = 'python'
    LOGGING_FILE_NAME = "icinga.log"
    BASE_LOG_PATH = os.path.join('var', 'log', 'splunk')
    LOGGING_FORMAT = "%(asctime)s %(levelname)-s\t%(module)s:%(lineno)d - %(message)s"
    splunk_log_handler = logging.handlers.RotatingFileHandler(os.path.join(SPLUNK_HOME, BASE_LOG_PATH, LOGGING_FILE_NAME), mode='a') 
    splunk_log_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
    logger.addHandler(splunk_log_handler)
    splunk.setupSplunkLogger(logger, LOGGING_DEFAULT_CONFIG_FILE, LOGGING_LOCAL_CONFIG_FILE, LOGGING_STANZA_NAME)
    return logger


def check_inputs(config, logger):
    setup_fields = ['host', 'port', 'user', 'pass']
    required_fields = ['type', 'filter', 'exit_status', 'plugin_output']
    
    for field in setup_fields:
        if not field in config:
            logger.error("No "+field+" specified. Have you configured the addon?")
            return False
    
    for field in required_fields:
        if not field in config:
            logger.error("No "+field+" specified.")
            return False
        
    return True


if len(sys.argv) > 1 and sys.argv[1] == "--execute":
    logger = setup_logging()
    alert = json.load(sys.stdin)
    if check_inputs(alert['configuration'], logger):
        #load config
        config = alert['configuration']

        #icinga API requires this header to accept data
        headers = {'Accept': 'application/json'}

        #construct URL
        url = "https://"+config['host']+":"+config['port']+"/v1/actions/process-check-result"

        #construct payload
        auth=(config['user'],config['pass'])
        payload = {}
        payload['type'] = config['type']
        payload['filter'] = config['filter']
        payload['exit_status'] = config['exit_status']
        payload['plugin_output'] = config['plugin_output']
        if 'performance_data' in config:
            payload['performance_data'] = config['performance_data']
        if 'check_command' in config:
            payload['check_command'] = config['check_command']
        if 'check_source' in config:
            payload['check_source'] = config['check_source']
        if 'execution_start' in config:
            payload['execution_start'] = config['execution_start']
        if 'execution_end' in config:
            payload['execution_end'] = config['execution_end']
        if 'ttl' in config:
            payload['ttl'] = config['ttl']

        #doit
        r = requests.post(url,auth=auth,headers=headers,json=payload,verify=False)
        if r.status_code == 200:
            logger.info("200: Success submitting passive check")
        else:
            logger.error(str(r.status_code)+": "+r.text)

    else:
        logger.error("Invalid configuration detected. Stopped.")
else:
    print("FATAL No execute flag given")
