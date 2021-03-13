
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
            varname="gmap",
            lat=EVENT_LOCATION[0],
            lng=EVENT_LOCATION[1],
            markers={
                icons.dots.green: [(EVENT_LOCATION[0], EVENT_LOCATION[1], 'Main Event!')],
                icons.dots.blue: [(A_MARKER[0], A_MARKER[1], 'Relevant Location')],
            },
            style=f'height:{set_height}px;width:{set_width}px;',
            zoom=16,
        )

        return gmap