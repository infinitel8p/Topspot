from kivy.garden.mapview import MapView
from kivy.app import App

class MapViewApp(App):
    def build(self):
        map = MapView(zoom=11, lat=51.41014850183159, lon=7.182447026769182)
        MapView.add_marker(lat=51.41014850183159, lon=7.182447026769182)
        return map

MapViewApp().run()

#https://www.youtube.com/watch?v=P940dd1VxsU