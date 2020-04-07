#Options for Icinga Passive Check Alert Action

action.icinga_passive_check = [0|1]
* Enable Iinga2 Passive Check Alert Action

action.icinga_passive_check.param.host= <string>
* Override global host of your Icinga2 instance API
* (optional)

action.icinga_passive_check.param.port = <int>
* Override Port to connect to Icinga2 API on. Usually 5665
* (optional)

action.icinga_passive_check.param.user = <string>
* Override API user name
* (optional)

action.icinga_passive_check.param.pass = <string>
* Override API user password
* (optional)

action.icinga_passive_check.param.type = [Service|Host]
* Type of check
* (required)

action.icinga_passive_check.param.filter = <string>
* Filter string for Icinga2. See https://icinga.com/docs/icinga2/latest/doc/12-icinga2-api/#filters
* (required)

action.icinga_passive_check.param.exit_status = [0|1|2|3]
* Exit status of the check. For services: 0=OK, 1=WARNING, 2=CRITICAL, 3=UNKNOWN, for hosts: 0=OK, 1=CRITICAL.
* (required)

action.icinga_passive_check.param.plugin_output = <string>
* Plugin output. Eg. "PING CRITICAL - Packet loss = 100%"
* (required)

action.icinga_passive_check.param.performance_data = <string>
* Plugin performance data. Can be comma separated. Eg. "rta=5000.000000ms;3000.000000;5000.000000;0.000000, pl=100%;80;100;0"
* (optional)

action.icinga_passive_check.param.check_command = <string>
* Check command used
* (optional)

action.icinga_passive_check.param.check_source = <string>
* Check source, usually the name of the command_endpoint
* (optional)

action.icinga_passive_check.param.execution_start = <string>
* The timestamp where a script/process started its execution.
* (optional)

action.icinga_passive_check.param.execution_end = <string>
* The timestamp where a script/process ended its execution.
* (optional)

action.icinga_passive_check.param.ttl = <int>
* Time-to-live duration in seconds for this check result.
* (optional)
