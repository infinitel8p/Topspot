from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard

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
                AsyncImage:
                    source: "https://images.unsplash.com/photo-1541963463532-d68292c34b19?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Ym9va3xlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80"
                    radius: [10,]
            MDSwiperItem:
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



MDScreen:

    MDToolbar:
        id: toolbar
        title: "Swiper APP"
        elevation: 10
        pos_hint: {"top": 1}
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
        self.status = 0
        return Builder.load_string(kv)

    def add_card(self):
        self.card = BlankMDCard()
        if not self.root.ids.card.children:
            if self.status == 0:
                self.status = 1
                self.root.ids.card.add_widget(self.card) # add the card to the enclosing layout
    def remove_card(self):
        if self.status == 1:
            self.status = 0
            self.root.ids.card.remove_widget(self.card)  # add the card to the enclosing layout# add the card to the enclosing layout


AddCardApp().run()