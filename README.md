Icinga Passive Check Alert Action
Adds an alert action to Splunk that allows sending a passive check result to Icinga2. [https://splunkbase.splunk.com/app/4944/](https://splunkbase.splunk.com/app/4944/)

This add-on requires the API feature to be enabled and an ApiUser created in Icinga2. Details on setting up the API are available in the Icinga2 documentation: [https://icinga.com/docs/icinga2/latest/doc/12-icinga2-api/](https://icinga.com/docs/icinga2/latest/doc/12-icinga2-api/)

Before using this add-on, it needs to be configured in Splunk. This can be done in the Splunk UI under *Settings>Alert Actions>Setup Icinga2 Passive Check Alert Action*. Alternatively, this can be done by updating and placing the below config in local/alert_actions.conf

    [icinga_passive_check]
    param.host = <<HOST/IP>>
    param.pass = <<PASSWORD>>
    param.port = <<PORT>> #Default is 5665
    param.user = <<USERNAME>>
