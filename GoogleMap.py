from flask_googlemaps import GoogleMaps, Map, icons

# Hardcoding some locations, to avoid too many google map requests
EVENT_LOCATION = [57.4627016845673, 9.983457412129107]
CHURCH_LOCATION = [57.45037451972904, 9.99648629863845]
CENTER = [57.45771117023997, 9.987441574012726]

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
            lat=CENTER[0],
            lng=CENTER[1],
            #markers={
            #    icons.dots.green: [(EVENT_LOCATION[0], EVENT_LOCATION[1], 'Main Event!')],
            #    icons.dots.blue: [(A_MARKER[0], A_MARKER[1], 'Relevant Location')]
            #},
            markers=[
                {
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                    'lat': EVENT_LOCATION[0],
                    'lng': EVENT_LOCATION[1],
                    'infobox': '<a target="_blank" href="https://www.google.com/maps/place/N%C3%B8rregade+22,+9800+Hj%C3%B8rring/@57.4625459,9.9813009,17z/data=!3m1!4b1!4m5!3m4!1s0x4648ce6fdb84f9fd:0xabe5f8efd947f34e!8m2!3d57.4625459!4d9.9834896">Vendelbohus</a>'
                },
                {
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                    'lat':CHURCH_LOCATION[0],
                    'lng': CHURCH_LOCATION[1],
                    'infobox': '<a target="_blank" href="https://www.google.com/maps/place/Bispensgade+67,+9800+Hj%C3%B8rring/@57.450236,9.9942976,17z/data=!3m1!4b1!4m5!3m4!1s0x4648ce0a9e3b671b:0x291eacc6982e8b2f!8m2!3d57.450236!4d9.9964863">Sankt Maria, martyrernes Dronning</a>'
                }
            ],
            style=f'height:{set_height}px;width:{set_width}px;',
            zoom=13.9,
            mapdisplay=True
        )

        return gmap