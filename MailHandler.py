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

class MailHandler(object):
    def __init__(self, logger, api_key, domain):
        self.logger = logger
        self.api_key = api_key
        self.domain = domain

    def send_mail(self):

        if request.method == 'POST':
            data = request.json
        
            post_mail = requests.post(
                f"https://api.mailgun.net/v3/{self.domain}/messages",
                auth=("api", self.api_key),
                data={"from": f"Bryllups Agent <secretagentman@{self.domain}>",
                    "to": ["mailguntest@clausnet.dk"],
                    "subject": f"RSVP fra {data['name']}",
                    "text": f"RSVP fra {data['name']}:\n\
                            Tlf: {data['phone']}\n\
                            Voksne: {data['adults']}, børn: {data['children']}\n\
                            Kommentar: {data['comment']}"})

            return Response(status=post_mail.status_code, mimetype='application/json')
