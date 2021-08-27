    def incoming(self, path, query_string, payload):
                if payload['issue']['severity']==5:
                        sevLevel='warning'
                elif payload['issue']['severity']==10:
                        sevLevel='minor'
                else:
                        sevLevel='indeterminate'
                if payload['issue']['type']=='incident':
                        sevLevel='critical'
                if payload['issue']['state']=='CLOSED':
                        serviceText='closed'
                        eventText='closed'
                        statusLevel='ack'
                        sevLevel='ok'
                        eventText='closed'
                        serviceText='closed'
                        resourceText='closed'
                        eventTags=['closed']

                if payload['issue']['state']=='OPEN':
                        statusLevel='open'
                        descriptionText='<a href="%s" target="_blank">View Issue in Instana Console</a>' % payload['issue']['link']
                        resourceText=payload['issue']['entityLabel']
                        serviceText=payload['issue']['service']
                        eventText='[' + payload['issue']['entityLabel'] + '] ' + payload ['issue']['text']
                        eventTags=[payload['issue']['tags']]

                return Alert(
                        id=payload['issue']['id'],
                        environment='Production',
                        status=statusLevel,
                        severity=sevLevel,
                        event=eventText,
                        text=descriptionText,
                        service=[serviceText],
                        resource=resourceText,
                        origin='Instana',
                        tags=eventTags,
                        raw_data=payload
                        )
