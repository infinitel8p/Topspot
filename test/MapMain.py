from kivymd.uix import screen
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy_garden.mapview import MapView, MapSource
from kivy_garden.mapview.view import MapMarker

class MapMainApp(MDApp):

    def button(self):
        print("working")

    def build(self):
        #print(MapSource.providers.keys())
        screen = MDScreen()

        map_view = MapView(lat=51.41014850183159, lon=7.182447026769182, zoom = 10)
        map_view.map_source = "osm"

        map_marker = MapMarker()
        map_marker.lat = 51.41014850183159
        map_marker.lon = 7.182447026769182
        map_marker.source = "map_marker.png"
        map_marker_button = MDFillRoundFlatButton()
        map_marker_button.on_press = self.button
        map_marker.add_widget(self.new_game_button)
        map_view.add_widget(map_marker)

        screen.add_widget(map_view)

        self.new_game_button = MDFillRoundFlatButton(
        text = "New Game",
        font_size = 30,
        pos_hint = {"center_x" : 0.5, "center_y" : 0.15},
        on_press = self.button)

        return screen

if __name__ == "__main__":
    MapMainApp().run()

#Test