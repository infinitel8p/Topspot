from kivymd.app import MDApp
import certifi
from kivy.network.urlrequest import UrlRequest
from urllib import parse
from kivymd.uix.snackbar import Snackbar


def ButtonCallback(address):
    global search_address
    search_address = address
    apikey = "alhPapHUB_qtDB3MT9R4wEud3UcR77RjD3fgTlHYiCE"
    address = parse.quote(address)
    url = f"https://geocoder.ls.hereapi.com/6.2/geocode.json?searchtext={address}&gen=9&apiKey={apikey}"
    UrlRequest(url, on_success=success_func, on_failure=failure,
               on_error=error, ca_file=certifi.where())


def success_func(urlrequest, result):
    try:
        latitude = result["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"]
        longitude = result["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"]
        print(longitude, latitude)
        app = MDApp.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(latitude, longitude)
        mapview.zoom = 13
    except IndexError:
        print(f"{IndexError} while searching for: {search_address}")
        Snackbar(
            text=f"'{search_address}' could not be found")


def failure(urlrequest, result):
    print("UrlRequest status: failure")
    print(result)


def error(urlrequest, result):
    print("UrlRequest status: error")
    print(result)
