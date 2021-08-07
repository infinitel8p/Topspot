from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivymd.app import MDApp

class SearchPopupMenu(MDInputDialog):
    title = "Search for a city"
    text_button_ok = "Search"

    def __init__(self):
        super().__init__()
        self.size_hint = [.6, .3]
        self.events_callback = self.callback

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)

    def geocode_get_lat_lon(self, address):
        apikey = "alhPapHUB_qtDB3MT9R4wEud3UcR77RjD3fgTlHYiCE"
        address = parse.quote(address)
        url = f"https://geocoder.ls.hereapi.com/6.2/geocode.json?searchtext={address}&gen=9&apiKey={apikey}"
        UrlRequest(url, on_success = self.success, on_failure = self.failure, on_error = self.error)

    def success(self, urlrequest, result):
        print("Success")
        try:
            latitude = result["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"]
            longitude = result["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"]
            print(longitude, latitude)
            app = MDApp.get_running_app()
            mapview = app.root.ids.mapview
            mapview.center_on(latitude, longitude)
        except IndexError:
            print(IndexError)

    def failure(self, urlrequest, result):
        print("Failure")
        print(result)

    def error(self, urlrequest, result):
        print("Error")
        print(result)