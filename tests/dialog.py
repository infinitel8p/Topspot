from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix import dialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.datatables import MDDataTable

KV = '''
<Item>

    ImageLeftWidget:
        source: root.source


MDFloatLayout:

    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_simple_dialog()
'''


class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()


class Example(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)

    def show_simple_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Set backup account",
                type="simple",
                buttons=[MDRaisedButton(text="Close", on_release=self.dialog_close),],
                items=[
                    Item(text="user01@gmail.com", source="user-1.png"),
                    Item(text="user02@gmail.com", source="user-2.png"),
                    Item(text="Add account", source="add-icon.png"),
                ],
            )
        self.dialog.open()


Example().run()
#https://kivymd.readthedocs.io/en/latest/components/dialog/index.html