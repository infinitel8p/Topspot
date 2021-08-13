from kivymd.uix.dialog import ListMDDialog
import requests
import certifi

class LocationPopupMenu(ListMDDialog):
    def __init__(self, spot_data):
        super().__init__()

        headers = ['nr', 'SpotName', 'x', 'y', 'MapsLink', 'Website', 'Street', 'City', 'Country', 'PLZ', 'Season1Date', 'Season1Time', 'Season2Date', 'Season2Time', 'Image1', 'Image2', 'Image3', 'Information', 'updateTime']

        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(spot_data[i])
            setattr(self, attribute_name, attribute_value)
        try:
            response = requests.get(str(self.Image1), verify=certifi.where())
            file = open(f"image1{self.SpotName}{self.nr}.png", "wb")
            file.write(response.content)
            file.close()
        except:
            response = requests.get("https://raw.githubusercontent.com/infinitel8p/Topspot/master/Images/missing.jpg", verify=certifi.where())
            file = open(f"image1{self.SpotName}{self.nr}.png", "wb")
            file.write(response.content)
            file.close()
        try:
            response = requests.get(str(self.Image2), verify=certifi.where())
            file = open(f"image2{self.SpotName}{self.nr}.png", "wb")
            file.write(response.content)
            file.close()
        except:
            response = requests.get("https://raw.githubusercontent.com/infinitel8p/Topspot/master/Images/missing.jpg", verify=certifi.where())
            file = open(f"image2{self.SpotName}{self.nr}.png", "wb")
            file.write(response.content)
            file.close()
        try:
            response = requests.get(str(self.Image3), verify=certifi.where())
            file = open(f"image3{self.SpotName}{self.nr}.png", "wb")
            file.write(response.content)
            file.close()
        except:
            response = requests.get("https://raw.githubusercontent.com/infinitel8p/Topspot/master/Images/missing.jpg", verify=certifi.where())
            file = open(f"image3{self.SpotName}{self.nr}.png", "wb")
            file.write(response.content)
            file.close()