
from flask_googlemaps import GoogleMaps, Map, icons

# Hardcoding some locations, to avoid too many google map requests
EVENT_LOCATION = [56.143218266395216, 8.994740213932541]
A_MARKER = [56.14352908145836, 8.993624414924469]

class GMap(object):
    def __init__(self, logger, app, api_key):
        self.logger = logger
        GoogleMaps(app, key=api_key)
    


    def get_map(self, height, width):
        set_height = 400
        set_width = 600
        if height is not None:
            set_height = height
        if width is not None:
            set_width = width
        
        gmap = Map(
            identifier="gmap",
            #varname="gmap",
            lat=EVENT_LOCATION[0],
            lng=EVENT_LOCATION[1],
            #markers={
            #    icons.dots.green: [(EVENT_LOCATION[0], EVENT_LOCATION[1], 'Main Event!')],
            #    icons.dots.blue: [(A_MARKER[0], A_MARKER[1], 'Relevant Location')]
            #},
            markers=[
                {
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                    'lat': EVENT_LOCATION[0],
                    'lng': EVENT_LOCATION[1],
                    'infobox': '<a target="_blank" href="https://www.google.com/maps/place/Herningsholmvej+7,+7400+Herning/@56.1430569,8.9925086,17z/data=!3m1!4b1!4m5!3m4!1s0x464bbc01922cc8cf:0x2bd3b6a7cc278f7d!8m2!3d56.1430569!4d8.9946972">Yay!</a>'
                },
                {
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                    'lat':A_MARKER[0],
                    'lng': A_MARKER[1],
                    'infobox': '<b>Hello World from other place</b>'
                }
            ],
            style=f'height:{set_height}px;width:{set_width}px;',
            zoom=16,
            mapdisplay=True
        )

        return gmap