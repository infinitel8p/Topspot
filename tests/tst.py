from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard

kv = """
<BlankMDCard>:
    orientation: "vertical"
    padding: "8dp"
    size_hint: None, None
    size: "280dp", "180dp"
    pos_hint: {"center_x": .5, "center_y": .5}

    MDLabel:
        text: "The Title Goes Here"
        theme_text_color: "Secondary"
        size_hint_y: None
        height: self.texture_size[1]

    MDSeparator:
        height: "1dp"

    MDLabel:
        text: "The Body"
    MDRaisedButton:
        text: 'Add MDCard'
        on_release: app.remove_card()
        pos_hint: {'center_x': 0.5}



MDBoxLayout:
    orientation: 'vertical'
    MDLabel:
        text: 'Add an MDCard Widget'
        halign: 'center'
        size_hint_y: None
        height: 24
    FloatLayout:
        id: card
    MDRaisedButton:
        text: 'Add MDCard'
        on_release: app.add_card()
        pos_hint: {'center_x': 0.5}
        

"""


class BlankMDCard(MDCard):
    pass


class AddCardApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def add_card(self):
        self.card = BlankMDCard()
        if not self.root.ids.card.children:
            self.root.ids.card.add_widget(self.card)  # add the card to the enclosing layout
    def remove_card(self):
        self.root.ids.card.remove_widget(self.card)  # add the card to the enclosing layout


AddCardApp().run()