from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from spotmarker import SpotMarker

class TopSpotMap(MapView):
    getting_spots_timer = None
    spot_names = []
    def start_getting_spots_in_fov(self):
        # After one second, get the spots in the field of view
        try:
            self.getting_spots_timer.cancel()
        except:
            pass

        self.getting_spots_timer = Clock.schedule_once(self.get_spots_in_fov, 1)

    def get_spots_in_fov(self, *args):
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()

        #sql_statement = "SELECT SpotName FROM spotlist WHERE x > %s AND x < %s AND y > %s AND y < %s"%(min_lon, max_lon, min_lat, max_lat)     AND x < {max_lon} AND y > {min_lat} AND y < {max_lat}
        sql_statement = f"SELECT * FROM spotlist WHERE x > {min_lon} AND x < {max_lon} AND y > {min_lat} AND y < {max_lat}"
        app.cursor.execute(sql_statement)
        spots = app.cursor.fetchall()

        print(f"Viewing: {self.get_bbox()}")
        print(spots)

        for spot in spots:
            name = spot[1]
            if name in self.spot_names:
                pass
            else:
                self.add_spot(spot)

    def add_spot(self, spot):
        print(f"Creating Marker for: {spot[1]}")
        print(spot[21], spot[20])

        #init marker for the spot
        lat, lon = spot[21], spot[20]
        marker = SpotMarker()
        marker.lat = lat
        marker.lon = lon
        marker.source = "map_marker_32x32.png"

        #add marker to map
        self.add_widget(marker)

        #register added markers
        name = spot[1]
        self.spot_names.append(name)


