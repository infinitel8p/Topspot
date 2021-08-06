from kivy_garden.mapview import MapView, MapMarker
from kivymd.app import MDApp
from kivymd.uix import screen
from kivymd.uix.screen import MDScreen

class App(MDApp):
    screen = MDScreen

class Map(MapView):
    map = MapView()
    map = MapView(zoom=9, lon=50.6394, lat=3.057)
    m1 = MapMarker(lon=50.6394, lat=3.057)  # Lille
    map.add_marker(m1)
    screen.add_widget(map)

App().run()