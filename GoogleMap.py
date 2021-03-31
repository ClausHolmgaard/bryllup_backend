from flask_googlemaps import GoogleMaps, Map, icons

# Hardcoding some locations, to avoid too many google map requests
EVENT_LOCATION = [57.4627016845673, 9.983457412129107]
CHURCH_LOCATION = [57.45037451972904, 9.99648629863845]
PARKING1_LOCATION = [57.46195301712721, 9.982948269583975]
PARKING2_LOCATION = [57.461981517010294, 9.985726883075484]
HOTEL_LOCATION = [57.45901640027358, 9.986475054455669]

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
                    # Party location
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                    'lat': EVENT_LOCATION[0],
                    'lng': EVENT_LOCATION[1],
                    'infobox': '<a target="_blank" href="https://www.google.com/maps/place/N%C3%B8rregade+22,+9800+Hj%C3%B8rring/@57.4625459,9.9813009,17z/data=!3m1!4b1!4m5!3m4!1s0x4648ce6fdb84f9fd:0xabe5f8efd947f34e!8m2!3d57.4625459!4d9.9834896">Vendelbohus</a>'
                },
                {
                    # Church Location
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                    'lat':CHURCH_LOCATION[0],
                    'lng': CHURCH_LOCATION[1],
                    'infobox': '<a target="_blank" href="https://www.google.com/maps/place/Sankt+Maria,+Martyrernes+Dronning/@57.4502159,9.9942672,17z/data=!3m1!4b1!4m5!3m4!1s0x4648cfbee50834ab:0xb224f403e75de60c!8m2!3d57.4502159!4d9.9964559">Sankt Maria, martyrernes Dronning</a>'
                },
                {
                    # Parking Location 1
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                    'lat':PARKING1_LOCATION[0],
                    'lng': PARKING1_LOCATION[1],
                    'infobox': '<a target="_blank" href="https://www.google.dk/maps/place/Kirkepladsen,p.+Pl.,+9800+Hj%C3%B8rring/@57.461803,9.9807703,17z/data=!3m1!4b1!4m5!3m4!1s0x4648ce6fd3d0d411:0xc9c19eeddd291736!8m2!3d57.461803!4d9.982959">Kirkepladsen, p. Plads</a>'
                },
                {
                    # Parking Location 2
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                    'lat':PARKING2_LOCATION[0],
                    'lng': PARKING2_LOCATION[1],
                    'infobox': '<a target="_blank" href="https://www.google.dk/maps/place/Sct+Olai+Pl.,+9800+Hj%C3%B8rring/@57.4618315,9.9835811,17z/data=!3m1!4b1!4m5!3m4!1s0x4648ce703105e45b:0xbab7420783927cb9!8m2!3d57.4618315!4d9.9857698">Sct. Olai Plads</a>'
                },
                {
                    # Hotel Location
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
                    'lat':HOTEL_LOCATION[0],
                    'lng': HOTEL_LOCATION[1],
                    'infobox': '<a target="_blank" href="https://www.google.dk/maps/place/Hotel+Ph%C3%B8nix+Hj%C3%B8rring/@57.4588606,9.98434,17z/data=!3m1!4b1!4m8!3m7!1s0x4648ce718388d947:0xa0e3a2b79bf9173e!5m2!4m1!1i2!8m2!3d57.4588606!4d9.9865287">Hotel Phønix Hjørring</a>'
                }
            ],
            style=f'height:{set_height}px;width:{set_width}px;',
            zoom=13.9,
            mapdisplay=True
        )

        return gmap