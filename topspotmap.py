from kivy_garden.mapview import MapView
from kivy.clock import Clock

class TopSpotMap(MapView):
    getting_spots_timer = None
    def start_getting_spots_in_fov(self):
        #load spots after 1 sec
        try:
            self.getting_spots_timer.cancel()
        except:
            pass

        self.getting_spots_timer = Clock.schedule_once(self.get_spots_in_fov, 1)

    def get_spots_in_fov(self, *args):
        print(self.get_bbox())