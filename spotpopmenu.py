from kivymd.uix.dialog import ListMDDialog
import urllib.request

class LocationPopupMenu(ListMDDialog):
    def __init__(self, spot_data):
        super().__init__()

        headers = ['ID', 'SpotName', 'x', 'y', 'MapsLink', 'Website', 'Street', 'City', 'Country', 'PLZ', 'Season1Date', 'Season1Time', 'Season2Date', 'Season2Time', 'Image1', 'Image2', 'Image3', 'Information', 'updateTime']

        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(spot_data[i])
            setattr(self, attribute_name, attribute_value)

        try:
            urllib.request.urlretrieve(str(self.Images), "image1.png")
        except:
            urllib.request.urlretrieve("https://raw.githubusercontent.com/infinitel8p/Topspot/master/Images/missing.jpg", "image1.png")

        try:
            urllib.request.urlretrieve(str(self.Images), "image2.png")
        except:
            urllib.request.urlretrieve("https://raw.githubusercontent.com/infinitel8p/Topspot/master/Images/missing.jpg", "image2.png")
        try:
             urllib.request.urlretrieve(str(self.Images), "image3.png")
        except:
            urllib.request.urlretrieve("https://raw.githubusercontent.com/infinitel8p/Topspot/master/Images/missing.jpg", "image3.png")