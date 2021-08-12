from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton

kv = """
<BlankMDCard>:

    orientation: "vertical"
    padding: "8dp"
    size_hint: 0.8, 0.8
    pos_hint: {"center_x": .5, "center_y": .5}

    RelativeLayout:
        adaptive_height: True
        spacing: "12dp"
        MDSwiper:
            size_hint_y: 1

            MDSwiperItem:
                FitImage:
                    AsyncImage:
                        source: "https://images.unsplash.com/photo-1541963463532-d68292c34b19?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Ym9va3xlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80"
                        radius: [10,]
                        texture: self.texture
            MDSwiperItem:
                FitImage:
                    AsyncImage:
                        source: "https://lh3.googleusercontent.com/proxy/XxXN99jBF8jqHLl3WznqDH1YB1WQ0RTvWZqTskkUT4vQxsAljzv_lV-TnC47RXdIjz4Y4SDwYj_HH9JxcNNzT7f0dmv1w0G4WmYdiYtNi74svGfxMApx4QId35OU7jHpg43KO01fhBymfA"
                        radius: [10,]
            MDSwiperItem:
                FitImage:
                    source: "Images\Screenshots\pic1_mobile.jpg"
                    radius: [10,]

    MDLabel:
        text: "The Title Goes Here"
        theme_text_color: "Secondary"
        size_hint_y: 0.2

    MDSeparator:
        height: "1dp"

    MDLabel:
        text: "The Body"
        size_hint_y: 0.2

    MDRaisedButton:
        text: 'Add MDCard'
        on_release: app.remove_card()
        pos_hint: {'center_x': 0.5}

"""


class BlankMDCard(MDCard):
    pass


class AddCardApp(MDApp):
    def build(self):
        self.status = 0
        self.screen = MDScreen()

        self.toolbar = MDToolbar(title = "Swiper APP")
        self.toolbar.id =  "toolbar"
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.orientation = 'vertical'
        self.screen.add_widget(self.toolbar)

        self.label = MDLabel()
        self.label.text = 'Add an MDCard Widget'
        self.label.halign = 'center'
        self.label.size_hint_y = None
        self.label.height = 24
        self.screen.add_widget(self.label)

        self.float_layout = MDFloatLayout()
        self.float_layout.id = "card"
        self.screen.add_widget(self.float_layout)

        self.button = MDRaisedButton()
        self.button.text = 'Add MDCard'
        self.button.on_release = self.add_card()
        self.button.pos_hint = {'center_x': 0.5}
        self.screen.add_widget(self.button)

        return self.screen

    def add_card(self):
        self.card = BlankMDCard()
        if self.status == 0:
            self.status = 1
            self.screen.add_widget(self.card) # add the card to the enclosing layout
    def remove_card(self):
        if self.status == 1:
            self.status = 0
            self.remove_widget(self.card)  # add the card to the enclosing layout# add the card to the enclosing layout

if __name__ == '__main__':
    AddCardApp().run()