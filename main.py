from kivymd.app import MDApp
import sqlite3
from topspotmap import TopSpotMap
from searchpopupmenu import SearchPopupMenu
from gpshelper import GpsHelper
import requests
import certifi

print("Beginning database download with urllib2...")
databse_url = "https://github.com/infinitel8p/Topspot/blob/master/spotlist.db?raw=true"
response = requests.get(databse_url, verify=certifi.where()) #verify=False
file = open("spotlist.db", "wb")
file.write(response.content)
file.close()
class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        self.theme_cls.primary_palette = "Blue" #['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        #init gps
        GpsHelper().run()
        TopSpotMap().start_getting_spots_in_fov()
        #init database
        self.connection = sqlite3.connect("spotlist.db")
        self.cursor = self.connection.cursor()
        #init SearchPopupMenu
        self.search_menu = SearchPopupMenu()

if __name__ == "__main__":
    MainApp().run()