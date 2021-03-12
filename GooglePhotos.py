import requests
import json
import re

image_url_pattern = re.compile('(?<=\[\\")https:\/\/lh3\.googleusercontent\.com\/[a-zA-Z0-9\-_]{2,}')

class GooglePhotos(object):

    def __init__(self, logger):
        self.logger = logger

    def get_from_url(self, url):
        r = requests.get(url=url, headers={'content-type':'application/json'})

        images = []
        for im_url in re.findall(image_url_pattern, r.text):
            images.append(im_url)
        
        #print(f'images: {list(set(images))}')

        return({'images': list(set(images))})