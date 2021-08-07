from kivy.garden.mapview import MapView
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

        self.getting_spots_timer = Clock.schedule_once(self.get_spots_in_fov, 0.5)

    def get_spots_in_fov(self, *args):
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = f"SELECT * FROM skatespots WHERE x > {min_lon} AND x < {max_lon} AND y > {min_lat} AND y < {max_lat}"
        app.cursor.execute(sql_statement)
        spots = app.cursor.fetchall()
        print(f"Seeing: {self.get_bbox()}")
        print(f"Spots in FOV: {len(spots)}")
        for spot in spots:
            name = spot[1]
            if name in self.spot_names:
                pass
            else:
                self.add_spot(spot)

    def add_spot(self, spot):
        print(f"Creating Marker for: {spot[1]} @ {spot[3]}, {spot[2]}")

        #init marker for the spot
        lat, lon = spot[3], spot[2]
        marker = SpotMarker()
        marker.lat = lat
        marker.lon = lon
        marker.source = "map_marker_32x32.png"
        marker.spot_data = spot
        #add marker to map
        self.add_widget(marker)
        #register added markers
        name = spot[1]
        self.spot_names.append(name)


