import requests
from flask import request, Response

REQUIRED_FIELDS = ['name',
                   'participating',
                   'email',
                   'adults',
                   'children0to3',
                   'children3to12',
                   'allergy']

class MailHandler(object):
    def __init__(self, logger, api_key, domain):
        self.logger = logger
        self.api_key = api_key
        self.domain = domain

    def send_mail(self):

        if request.method == 'POST':
            data = request.json

            missing_fields = []
            for r in REQUIRED_FIELDS:
                if not(r in data):
                    missing_fields.append(r)

            if(len(missing_fields) > 0):
                status_text = f"{{'Fields_missing': '{','.join(missing_fields)}'}}"
                return Response(status_text, status=400, mimetype='application/json')
            
            deltager = 'ja'
            if data['participating'] == 'false':
                deltager = 'nej'
        
            post_mail = requests.post(
                f"https://api.mailgun.net/v3/{self.domain}/messages",
                auth=("api", self.api_key),
                data={"from": f"Bryllups Agent <secretagentman@{self.domain}>",
                    "to": ["rsvp@buiholmgaard.dk"],
                    "subject": f"RSVP fra {data['name']}",
                    "text": f"RSVP fra {data['name']}:\n\
                            Deltager: {deltager}\n\
                            Email: {data['email']}\n\
                            Voksne: {data['adults']}\n\
                            Børn under 3: {data['children0to3']}\n\
                            Børn 3 til 12: {data['children3to12']}\n\
                            Allergier: {data['allergy']}"})

            return Response(status=post_mail.status_code, mimetype='application/json')
