import os
import logging
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

from GooglePhotos import GooglePhotos
from GoogleMap import GMap
from MailHandler import MailHandler

cors_config = {
  "origins": ["http://localhost:5000"],
  "methods": ["OPTIONS", "GET", "POST"],
  "allow_headers": ["Authorization", "Content-Type"]
}

mailgun_api_key = os.environ['MAILGUN_API_KEY']
mailgun_domain = os.environ['MAILGUN_DOMAIN']
google_map_key = os.environ['BRYLLUP_GOOGLE_MAP_KEY']
image_url = 'https://photos.app.goo.gl/Qkvp72b5QoqAuWy86'

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, template_folder='.')
CORS(app, resources={"/*": cors_config})

gphotos = GooglePhotos(app.logger)
gmap = GMap(app.logger, app, google_map_key)
mailer = MailHandler(app.logger, mailgun_api_key, mailgun_domain)

@app.route('/hello')
def hello():
    return {'hello': 'world'}

@app.route('/map')
def google_map():
    height = request.args.get('height')
    width = request.args.get('width')

    #return render_template('MapTemplate.html', mymap=gmap.get_map()[0], sndmap=gmap.get_map()[1])
    return render_template('MapTemplate.html', gmap=gmap.get_map(height, width))

@app.route('/mail', methods=['POST'])
def send_mail():
    return mailer.send_mail()

@app.route('/images')
def image_list():
    return jsonify(gphotos.get_from_url(image_url))

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Accept,Content-Type,Authorization'
    header['Access-Control-Allow-Methods'] = 'GET,POST'
    return response

if __name__ == '__main__':
    app.run(debug=True)