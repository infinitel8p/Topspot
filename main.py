from kivymd.app import MDApp
import sqlite3
from topspotmap import TopSpotMap
class MainApp(MDApp):
    connection = None
    cursor = None
    def on_start(self):
        #init gps
        #init database
        self.connection = sqlite3.connect("markets.db")
        self.cursor = self.connection.cursor()
        #init SearchPopupMenu

if __name__ == "__main__":
    MainApp().run()


#https://youtu.be/qP9KYWrrORY?t=669
#https://mungingdata.com/sqlite/create-database-load-csv-python/