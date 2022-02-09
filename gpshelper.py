from kivymd.app import MDApp
from kivy.utils import platform
from lib.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar


class GpsHelper():
    has_centered_map = False

    def run(self):
        # reference the blinker
        gps_blinker = MDApp.get_running_app().root.ids.mapview.ids.blinker
        # start blinking to show position
        gps_blinker.blink()
        # request permissions on android
        if platform == "android":
            from android.permissions import request_permissions, Permission

            def callback(permission, results):
                if all([res for res in results]):
                    print("Got all permissions")
                else:
                    print("Did not get all permissions")
            request_permissions(
                [Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION], callback)
        # configure gps
        if platform == "android" or platform == "ios":
            from plyer import gps
            try:
                gps.configure(on_location=self.update_blinker_position,
                              on_status=self.on_auth_status)
                gps.start(minTime=1000, minDistance=0)
            except:
                Snackbar(
                    text=f"No GPS! Please check/enable GPS and restart the app.").open()
        # else:
            # update gps coordinates on screen
        #    coordinate_label = MDApp.get_running_app().root.ids.coordinate_label
        #    min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        #    coordinate_label.text = f"GPS Coordinates:\nlat: {(min_lat+max_lat)/2}\nlon: {(min_lon+max_lon)/2}"

    def update_blinker_position(self, *args, **kwargs):
        try:
            global my_lat
            my_lat = kwargs["lat"]
            global my_lon
            my_lon = kwargs["lon"]
            print("GPS Position:", my_lat, my_lon)
            # update blinkerpos
            gps_blinker = MDApp.get_running_app().root.ids.mapview.ids.blinker
            gps_blinker.lat = my_lat
            gps_blinker.lon = my_lon
            # center map on gps
            if not self.has_centered_map:
                map = MDApp.get_running_app().root.ids.mapview
                map.center_on(my_lat, my_lon)
                map.zoom = 14
                self.has_centered_map = True
        except:
            Snackbar(
                text=f"No GPS! Please check/enable GPS and restart the app.").open()

    def gps_button_callback():
        if platform == "android" or platform == "ios":
            try:
                map = MDApp.get_running_app().root.ids.mapview
                map.center_on(my_lat, my_lon)
                map.zoom = 15
            except:
                Snackbar(
                    text=f"No GPS! Please check/enable GPS and restart the app.").open()
        else:
            map = MDApp.get_running_app().root.ids.mapview
            map.center_on(52.51625163358924, 13.377699466276058)
            map.zoom = 15

    def on_auth_status(self, general_status, status_message):
        if general_status == "provider-enabled":
            pass
        else:
            self.open_gps_access_popup()

    def open_gps_access_popup(self):
        dialog = MDDialog()
        dialog.title = "GPS Error"
        dialog.text = "You need to enable GPS for the app to be able to fetch the spots and work properly!"
        dialog.size_hint = [.8, .8]
        dialog.pos_hint = {"center_x": .5, "center_y": .5}
        dialog.open()
