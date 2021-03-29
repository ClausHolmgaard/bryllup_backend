import requests
from flask import request, Response

"""
def send_complex_message():
    return requests.post(
        "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
        auth=("api", "YOUR_API_KEY"),
        files=[("attachment", ("test.jpg", open("files/test.jpg","rb").read())),
               ("attachment", ("test.txt", open("files/test.txt","rb").read()))],
        data={"from": "Excited User <YOU@YOUR_DOMAIN_NAME>",
              "to": "foo@example.com",
              "cc": "baz@example.com",
              "bcc": "bar@example.com",
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!",
              "html": "<html>HTML version of the body</html>"})
"""

REQUIRED_FIELDS = ['name',
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
            
        
            post_mail = requests.post(
                f"https://api.mailgun.net/v3/{self.domain}/messages",
                auth=("api", self.api_key),
                data={"from": f"Bryllups Agent <secretagentman@{self.domain}>",
                    "to": ["rsvp@buiholmgaard.dk"],
                    "subject": f"RSVP fra {data['name']}",
                    "text": f"RSVP fra {data['name']}:\n\
                            Email: {data['email']}\n\
                            Voksne: {data['adults']}\n\
                            Børn under 3: {data['children0to3']}\n\
                            Børn 3 til 12: {data['children3to12']}\n\
                            Allergier: {data['allergy']}"})

            return Response(status=post_mail.status_code, mimetype='application/json')
