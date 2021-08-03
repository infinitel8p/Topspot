from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy_garden.mapview import MapView, MapSource
from kivy_garden.mapview.view import MapMarker

class MapMainApp(App):

    def build(self):
        #print(MapSource.providers.keys())
        box_layout = BoxLayout()

        map_view = MapView(lat=51.41014850183159, lon=7.182447026769182, zoom = 10)
        map_view.map_source = "osm"

        map_marker = MapMarker()
        map_marker.lat = 51.41014850183159
        map_marker.lon = 7.182447026769182
        map_marker.source = "map_marker.png"
        map_marker_button = Button()
        map_marker_button.on_press = print("hello")
        map_marker.add_widget(map_marker_button)
        map_view.add_widget(map_marker)


        box_layout.add_widget(map_view)

        return box_layout

if __name__ == "__main__":
    MapMainApp().run()