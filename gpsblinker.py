from kivy.garden.mapview import MapMarker
from kivy.animation import Animation

class GpsBlinker(MapMarker):
    def blink(self):
        # animation for blink size & marker opacity
        animatio = Animation(opacity = 0, blink_size = 30)
        animatio.bind(on_complete = self.reset)
        animatio.start(self)

    def reset(self, *args):
        self.opacity = 1
        self.blink_size = self.default_blink_size
        self.blink()