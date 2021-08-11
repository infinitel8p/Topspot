from kivy.uix.modalview import ModalView
from kivy.lang import Builder

from kivymd import images_path
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

Builder.load_string(
    '''
<Card>:
    elevation: 20
    orientation: "vertical"
    padding: "8dp"
    size_hint: 1.6,1.1
    pos_hint: {"center_x": .5, "center_y": .5}
    Carousel:
        FitImage:
            id: bg_image
            source: "Images/TopSpotLogo.jpg"
            size_hint_y: .4
            pos_hint: {"top": 1}
        FitImage:
            id: bg_image
            size_hint_y: .4
            pos_hint: {"top": 1}
            source: "Images/TopSpotGrey.jpg"
''')

class Card(MDCard):
    pass


class Example(MDApp):
    def build(self):
        modal = ModalView(
            size_hint=(0.4, 0.8),
            background=f"{images_path}/transparent.png",
            overlay_color=(0, 0, 0, 0),
        )
        modal.add_widget(Card())
        modal.open()


Example().run()