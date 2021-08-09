from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.card import MDCard, MDSeparator

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.image import AsyncImage

Builder.load_string("""
<AppScreen>:
    MDBoxLayout:
        canvas.before:
            Color:
                rgba:1,0,0,1 #Red
            Rectangle:
                size:self.size
                pos:self.pos

        orientation:'vertical'
        pos_hint: {'center_x':.5, 'center_y':.4}
        size_hint: (.75, .6)

        ScrollView:
            canvas.before:
                Color:
                    rgba: 0,1,0,.5 #Green
                Rectangle:
                    size:self.size
                    pos:self.pos 
            do_scroll_x:False
            do_scroll_y:True
            pos_hint:{'center_x':0.5, 'center_y':0.5}
            size_hint:(0.5,1)
            MDBoxLayout:
                canvas.before:
                    Color:
                        rgba: 0,0,1,.5
                    Rectangle:
                        size:self.size
                        pos:self.pos 
                orientation:'vertical'
                id:container
                size_hint_y:None #This makes the stuff scroll O.o
                height:self.minimum_height
                spacing:10

    MDRectangleFlatButton:
        text:"Press Me"
        pos_hint:{'center_x':0.5, 'center_y':.8}
        on_release:root.printing()
""")

class AppScreen(Screen):
    def __init__(self, **kwargs):
        super(AppScreen, self).__init__(**kwargs)
        self.scroll_id = self.ids.container
    def printing(self):
        for x in range(5):
            img=AsyncImage(
                source="https://i.redd.it/x1js663rq7s41.jpg",
                pos_hint={'center_x':0.9, 'center_y':0.5},
                size_hint_y=None,
                size=(dp(20), dp(30))
                )
            card = MDCard(
                orientation='vertical',
                pos_hint={'center_x':0.5},
                size_hint=(1, None),
                #size=(dp(100), dp(100)) #Size is required to view stuff in Cards

            )
            card.add_widget(img)
            self.scroll_id.add_widget(card)
class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        return AppScreen()

DemoApp().run()