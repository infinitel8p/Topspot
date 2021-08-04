from kivymd.uix import screen
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy_garden.mapview import MapView, MapSource
from kivy_garden.mapview.view import MapMarker

class MapMainApp(MDApp):

    def build(self):
        #print(MapSource.providers.keys())
        Screen = screen()

        map_view = MapView(lat=51.41014850183159, lon=7.182447026769182, zoom = 10)
        map_view.map_source = "osm"

        map_marker = MapMarker()
        map_marker.lat = 51.41014850183159
        map_marker.lon = 7.182447026769182
        map_marker.source = "map_marker.png"
        map_view.add_widget(map_marker)

        screen.add_widget(map_view)
        return Screen

if __name__ == "__main__":
    MapMainApp().run()

#Test