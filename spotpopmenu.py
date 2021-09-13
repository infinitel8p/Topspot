from dialog import ListMDDialog
import requests
import certifi
import shutil
import os.path
import filecmp


def ImageCheck(imageSource, imageName, fileName, SpotName, iD):
    try:
        # Check if image is already downloaded/created and if it is different to the error.png
        if os.path.isfile(f"cache/{fileName}{SpotName}{iD}.png") and filecmp.cmp(f"cache/{fileName}{SpotName}{iD}.png", "error.png") == False:
            print('[' + '\x1b[1;32;40m' + 'INFO' + '\x1b[0m' +
                  f'   ] [{imageName}     ] ' + "Check succedeed - Image found - Cached Image will be used")
        # If image cannot be used from cache try to download the image
        else:
            print('[' + '\x1b[1;33;40m' + 'INFO' + '\x1b[0m' +
                  f'   ] [{imageName}     ] ' + "Cache check failed - Image will be downloaded")
            # Download image if the image link in database is not empty
            if imageSource != "":
                print('[' + '\x1b[1;32;40m' + 'INFO' + '\x1b[0m' +
                      f'   ] [{imageName}     ] ' + f"Found Image source - using {imageSource}")
                response = requests.get(
                    str(imageSource), verify=certifi.where())
                file = open(f"cache/{fileName}{SpotName}{iD}.png", "wb")
                file.write(response.content)
                file.close()
            # Use the missing.jpg if there is no image link in database
            else:
                print('[' + '\x1b[1;31;40m' + 'INFO' + '\x1b[0m' +
                      f'   ] [{imageName}     ] ' + "Missing Image - using missing.jpg")
                shutil.copy("missing.jpg",
                            f"cache/{fileName}{SpotName}{iD}.png")
    except:
        print('[' + '\x1b[1;31;40m' + 'INFO' + '\x1b[0m' +
              f'   ] [{imageName}     ] ' + "Download failed - Device Offline, using error.png")
        shutil.copy("error.png", f"cache/{fileName}{SpotName}{iD}.png")


class LocationPopupMenu(ListMDDialog):
    def __init__(self, spot_data):
        super().__init__()

        headers = ['ID', 'SpotName', 'x', 'y', 'MapsLink', 'Website', 'Street', 'City',
                   'Country', 'PLZ', 'Image1', 'Image2', 'Image3', 'Information', 'updateTime']

        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(spot_data[i])
            setattr(self, attribute_name, attribute_value)
        ImageCheck(self.Image1, "Image 1", "image1", self.SpotName, self.ID)
        ImageCheck(self.Image2, "Image 2", "image2", self.SpotName, self.ID)
        ImageCheck(self.Image3, "Image 3", "image3", self.SpotName, self.ID)
