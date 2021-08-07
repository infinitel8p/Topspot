from spotpopmenu import LocationPopupMenu
from kivy.garden.mapview import MapMarkerPopup, MapMarker
from spotpopmenu import LocationPopupMenu

class SpotMarker(MapMarkerPopup):
    spot_data = []

    def on_release(self):
        menu = LocationPopupMenu(self.spot_data)
        menu.size_hint = [.8,.8]
        menu.open()

