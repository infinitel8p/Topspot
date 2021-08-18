import certifi
from kivy.clock import Clock
from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDFlatButton


class SearchPopupMenu(MDInputDialog):
    title = "Search for a city"
    text_button_ok = "Search"

    def __init__(self):
        super().__init__()
        self.size_hint = [.8, .3]
        self.events_callback = self.callback

    def open(self, *args):
        super().open()
        Clock.schedule_once(self.set_field_focus, 0.5)

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)

    def geocode_get_lat_lon(self, address):
        apikey = "alhPapHUB_qtDB3MT9R4wEud3UcR77RjD3fgTlHYiCE"
        address = parse.quote(address)
        url = f"https://geocoder.ls.hereapi.com/6.2/geocode.json?searchtext={address}&gen=9&apiKey={apikey}"
        UrlRequest(url, on_success=self.success, on_failure=self.failure,
                   on_error=self.error, ca_file=certifi.where())

    def success(self, urlrequest, result):
        print("UrlRequest status: successful")
        try:
            latitude = result["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"]
            longitude = result["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"]
            print(longitude, latitude)
            app = MDApp.get_running_app()
            mapview = app.root.ids.mapview
            mapview.center_on(latitude, longitude)
        except IndexError:
            print(f"{IndexError} while searching for: {self.text_field.text}")
            Snackbar(
                text=f"'{self.text_field.text}' could not be found",
                button_text="RETRY",
                button_callback=self.open).show()

    def failure(self, urlrequest, result):
        print("UrlRequest status: failure")
        print(result)

    def error(self, urlrequest, result):
        print("UrlRequest status: error")
        print(result)
