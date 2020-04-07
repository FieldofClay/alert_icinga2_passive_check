import sys, requests, json, re

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def check_inputs(config):
    setup_fields = ['host', 'port', 'user', 'pass']
    required_fields = ['type', 'filter', 'exit_status', 'plugin_output']
    
    for field in setup_fields:
        if not field in config:
            eprint("ERROR No "+field+" specified. Have you configured the addon?")
            return False
    
    for field in required_fields:
        if not field in config:
            eprint("ERROR, No "+field+" specified.")
            return False
        
    return True


if len(sys.argv) > 1 and sys.argv[1] == "--execute":
    alert = json.load(sys.stdin)
    if check_inputs(alert['configuration']):
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
        if 'execuution_start' in config:
            payload['execution_start'] = config['execution_start']
        if 'execution_end' in config:
            payload['execution_end'] = config['execution_end']
        if 'ttl' in config:
            payload['ttl'] = config['ttl']

        #doit
        r = requests.post(url,auth=auth,headers=headers,json=payload,verify=False)
        if r.status_code == 200:
            eprint("INFO 200: Success submitting passive check")
        else:
            eprint("ERROR "+str(r.status_code)+": "+r.text)

    else:
        eprint("ERROR Invalid configuration detected. Stopped.")
else:
    eprint("FATAL No execute flag given")
