from kivymd.uix.dialog import ListMDDialog
import requests
import certifi
import shutil
import os.path
import filecmp


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
            if os.path.isfile(f"image1{self.SpotName}{self.ID}.png") and filecmp.cmp(f"image1{self.SpotName}{self.ID}.png", "error.png") == False:
                print('[' + '\x1b[1;32;40m' + 'INFO' + '\x1b[0m' +
                      '   ] [Image1      ] ' + "Check succedeed - Image found - Cached Image will be used")
            else:
                print('[' + '\x1b[1;33;40m' + 'INFO' + '\x1b[0m' +
                      '   ] [Image1      ] ' + "Cache check failed - Image will be downloaded")
                if self.Image1 != "":
                    print('[' + '\x1b[1;32;40m' + 'INFO' + '\x1b[0m' +
                          '   ] [Image1      ] ' + f"Found Image source - using {self.Image1}")
                    response = requests.get(
                        str(self.Image1), verify=certifi.where())
                    file = open(f"image1{self.SpotName}{self.ID}.png", "wb")
                    file.write(response.content)
                    file.close()
                else:
                    print('[' + '\x1b[1;31;40m' + 'INFO' + '\x1b[0m' +
                          '   ] [Image1      ] ' + "Missing Image - using missing.jpg")
                    response = requests.get(
                        "https://raw.githubusercontent.com/infinitel8p/Topspot/master/Images/missing.jpg", verify=certifi.where())
                    file = open(f"image1{self.SpotName}{self.ID}.png", "wb")
                    file.write(response.content)
                    file.close()
        except:
            print('[' + '\x1b[1;31;40m' + 'INFO' + '\x1b[0m' +
                  '   ] [Image1      ] ' + "Download failed - Device Offline, using error.png")
            shutil.copy("error.png", f"image1{self.SpotName}{self.ID}.png")

        try:
            if os.path.isfile(f"image1{self.SpotName}{self.ID}.png") and filecmp.cmp(f"image1{self.SpotName}{self.ID}.png", "error.png") == False:
                print('[' + '\x1b[1;32;40m' + 'INFO' + '\x1b[0m' +
                      '   ] [Image2      ] ' + "Check succedeed - Image found - Cached Image will be used")
            else:
                print('[' + '\x1b[1;33;40m' + 'INFO' + '\x1b[0m' +
                      '   ] [Image2      ] ' + "Cache check failed - Image will be downloaded")
                if self.Image2 != "":
                    print('[' + '\x1b[1;32;40m' + 'INFO' + '\x1b[0m' +
                          '   ] [Image2      ] ' + f"Found Image source - using {self.Image2}")
                    response = requests.get(
                        str(self.Image2), verify=certifi.where())
                    file = open(f"image2{self.SpotName}{self.ID}.png", "wb")
                    file.write(response.content)
                    file.close()
                else:
                    print('[' + '\x1b[1;31;40m' + 'INFO' + '\x1b[0m' +
                          '   ] [Image2      ] ' + "Missing Image - using missing.jpg")
                    response = requests.get(
                        "https://raw.githubusercontent.com/infinitel8p/Topspot/master/Images/missing.jpg", verify=certifi.where())
                    file = open(f"image2{self.SpotName}{self.ID}.png", "wb")
                    file.write(response.content)
                    file.close()
        except:
            print('[' + '\x1b[1;31;40m' + 'INFO' + '\x1b[0m' +
                  '   ] [Image2      ] ' + "Download failed - Device Offline, using error.png")
            shutil.copy("error.png", f"image2{self.SpotName}{self.ID}.png")

        try:
            if os.path.isfile(f"image1{self.SpotName}{self.ID}.png") and filecmp.cmp(f"image1{self.SpotName}{self.ID}.png", "error.png") == False:
                print('[' + '\x1b[1;32;40m' + 'INFO' + '\x1b[0m' +
                      '   ] [Image3      ] ' + "Check succedeed - Image found - Cached Image will be used")
            else:
                print('[' + '\x1b[1;33;40m' + 'INFO' + '\x1b[0m' +
                      '   ] [Image3      ] ' + "Check failed - Image will be downloaded")
                if self.Image3 != "":
                    print('[' + '\x1b[1;32;40m' + 'INFO' + '\x1b[0m' +
                          '   ] [Image3      ] ' + f"Found Image source - using {self.Image3}")
                    response = requests.get(
                        str(self.Image3), verify=certifi.where())
                    file = open(f"image3{self.SpotName}{self.ID}.png", "wb")
                    file.write(response.content)
                    file.close()
                else:
                    print('[' + '\x1b[1;31;40m' + 'INFO' + '\x1b[0m' +
                          '   ] [Image3      ] ' + "Missing Image - using missing.jpg")
                    response = requests.get(
                        "https://raw.githubusercontent.com/infinitel8p/Topspot/master/Images/missing.jpg", verify=certifi.where())
                    file = open(f"image3{self.SpotName}{self.ID}.png", "wb")
                    file.write(response.content)
                    file.close()
        except:
            print('[' + '\x1b[1;31;40m' + 'INFO' + '\x1b[0m' +
                  '   ] [Image3      ] ' + "Download failed - Device Offline, using error.png")
            shutil.copy("error.png", f"image3{self.SpotName}{self.ID}.png")
