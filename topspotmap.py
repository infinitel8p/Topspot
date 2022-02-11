from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivymd.app import MDApp
from spotmarker import SpotMarker
from kivy.utils import platform


class TopSpotMap(MapView):
    getting_spots_timer = None
    spot_names = []

    def start_getting_spots_in_fov(self):
        # After one second, get the spots in the field of view
        try:
            self.getting_spots_timer.cancel()
        except:
            pass

        self.getting_spots_timer = Clock.schedule_once(
            self.get_spots_in_fov, 0.5)

    def get_spots_in_fov(self, *args):
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = MDApp.get_running_app()
        sql_statement = f"SELECT * FROM skatespots WHERE x > {min_lon} AND x < {max_lon} AND y > {min_lat} AND y < {max_lat}"
        app.cursor.execute(sql_statement)
        spots = app.cursor.fetchall()
        print('[' + '\x1b[1;35;40m' + 'INFO' + '\x1b[0m' +
              '   ] [Mapview     ] ' + "Seeing: " + '\x1b[1;35;40m' + f"{self.get_bbox()}" +
              '\x1b[0m')
        print('[' + '\x1b[1;35;40m' + 'INFO' + '\x1b[0m' +
              '   ] [Mapview     ] ' + "Spots in FOV: " + '\x1b[1;35;40m' + f"{len(spots)}" +
              '\x1b[0m')
        for spot in spots:
            name = spot[1]
            if name in self.spot_names:
                pass
            else:
                self.add_spot(spot)
        # update gps coordinates on screen
        if platform == "android" or platform == "ios":
            coordinate_label = MDApp.get_running_app().root.ids.coordinate_label
            gps_blinker = MDApp.get_running_app().root.ids.mapview.ids.blinker
            coordinate_label.text = f"GPS Coordinates:\nlat: {round(gps_blinker.lat, 4)}\nlon: {round(gps_blinker.lon, 4)}\nSpots in FOV: {len(spots)}"
        else:
            # update gps coordinates on screen
            coordinate_label = MDApp.get_running_app().root.ids.coordinate_label
            coordinate_label.text = f"GPS Coordinates:\nlat: {round((min_lat+max_lat)/2, 4)}\nlon: {round((min_lon+max_lon)/2, 4)}\nSpots in FOV: {len(spots)}"

    def add_spot(self, spot):
        print('[' + '\x1b[1;34;40m' + 'INFO' + '\x1b[0m' +
              '   ] [Mapview     ] ' + "Creating Marker for: " +
              '\x1b[1;34;40m' + f"{spot[1]}" + '\x1b[0m' + f" @ {spot[3]}, {spot[2]}")

        if spot[14] == "Skatepark":
            # init red marker for skateparks
            lat, lon = spot[3], spot[2]
            marker = SpotMarker()
            marker.lat = lat
            marker.lon = lon
            marker.source = "lib/map_marker2_32x32.png"
            marker.spot_data = spot
            # add marker to map
            self.add_widget(marker)
            # register added markers
            name = spot[1]
            self.spot_names.append(name)

        else:
            # init blue marker for the spot
            lat, lon = spot[3], spot[2]
            marker = SpotMarker()
            marker.lat = lat
            marker.lon = lon
            marker.source = "lib/map_marker_32x32.png"
            marker.spot_data = spot
            # add marker to map
            self.add_widget(marker)
            # register added markers
            name = spot[1]
            self.spot_names.append(name)
