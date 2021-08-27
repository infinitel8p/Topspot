from kivymd.uix.dialog import ListMDDialog
import requests
import certifi
import shutil


class LocationPopupMenu(ListMDDialog):
    def __init__(self, spot_data):
        super().__init__()

        headers = ['ID', 'SpotName', 'x', 'y', 'MapsLink', 'Website', 'Street', 'City',
                   'Country', 'PLZ', 'Image1', 'Image2', 'Image3', 'Information', 'updateTime']

        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(spot_data[i])
            setattr(self, attribute_name, attribute_value)
        try:
            if self.Image1 != "":
                response = requests.get(
                    str(self.Image1), verify=certifi.where())
                file = open(f"image1{self.SpotName}{self.ID}.png", "wb")
                file.write(response.content)
                file.close()
            else:
                response = requests.get(
                    "https://raw.githubusercontent.com/infinitel8p/Topspot/master/Images/missing.jpg", verify=certifi.where())
                file = open(f"image1{self.SpotName}{self.ID}.png", "wb")
                file.write(response.content)
                file.close()
        except:
            shutil.copy("error.png", f"image1{self.SpotName}{self.ID}.png")

        try:
            if self.Image2 != "":
                response = requests.get(
                    str(self.Image2), verify=certifi.where())
                file = open(f"image2{self.SpotName}{self.ID}.png", "wb")
                file.write(response.content)
                file.close()
            else:
                response = requests.get(
                    "https://raw.githubusercontent.com/infinitel8p/Topspot/master/Images/missing.jpg", verify=certifi.where())
                file = open(f"image2{self.SpotName}{self.ID}.png", "wb")
                file.write(response.content)
                file.close()
        except:
            shutil.copy("error.png", f"image2{self.SpotName}{self.ID}.png")

        try:
            if self.Image3 != "":
                response = requests.get(
                    str(self.Image3), verify=certifi.where())
                file = open(f"image3{self.SpotName}{self.ID}.png", "wb")
                file.write(response.content)
                file.close()
            else:
                response = requests.get(
                    "https://raw.githubusercontent.com/infinitel8p/Topspot/master/Images/missing.jpg", verify=certifi.where())
                file = open(f"image3{self.SpotName}{self.ID}.png", "wb")
                file.write(response.content)
                file.close()
        except:
            shutil.copy("error.png", f"image3{self.SpotName}{self.ID}.png")
