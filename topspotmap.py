from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App

class TopSpotMap(MapView):
    getting_spots_timer = None

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
        sql_statement = "SELECT * FROM spotlist WHERE x > %s AND x < %s AND y > %s AND y < %s "%(min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(sql_statement)
        spots = app.cursor.fetchall()
        print(spots)
        for spot in spots:
            self.add_spot(spot)

    def add_spot(self, spot):
        pass


