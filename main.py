from kivymd.app import MDApp
import sqlite3
from topspotmap import TopSpotMap
from searchpopupmenu import SearchPopupMenu
from gpshelper import GpsHelper
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
import requests
import certifi


class MainApp(MDApp):
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.theme_cls.primary_palette = "Blue"

        # init gps
        try:
            print("Beginning database download with urllib2...")
            databse_url = "https://github.com/infinitel8p/Topspot/blob/master/spotlist.db?raw=true"
            response = requests.get(
                databse_url, verify=certifi.where())  # verify=False
            file = open("spotlist.db", "wb")
            file.write(response.content)
            file.close()
            print(
                "Download and writing database completed\nApplication main loop will be started...")
        except:
            pass
        GpsHelper().run()
        TopSpotMap().start_getting_spots_in_fov()

        # init database
        self.connection = sqlite3.connect("spotlist.db")
        self.cursor = self.connection.cursor()

        # init SearchPopupMenu
        self.search_menu = SearchPopupMenu()


if __name__ == "__main__":
    MainApp().run()
