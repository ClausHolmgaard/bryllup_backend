import logging
from flask import Flask, jsonify
from flask_restx import Api, Resource

from GooglePhotos import GooglePhotos

#image_url = 'https://photos.app.goo.gl/hj5od1ctFPdXnH739'
image_url = 'https://photos.app.goo.gl/Qkvp72b5QoqAuWy86'

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
api = Api(app=app,
          title="Simple app",
          description="Simple app")

gphotos = GooglePhotos(app.logger)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/images')
class Images(Resource):
    def get(self):
        return jsonify(gphotos.get_from_url(image_url))

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)