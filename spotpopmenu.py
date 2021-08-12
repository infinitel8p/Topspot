from kivymd.uix.dialog import ListMDDialog

class LocationPopupMenu(ListMDDialog):
    def __init__(self, spot_data):
        super().__init__()

        headers = ['ID', 'SpotName', 'x', 'y', 'MapsLink', 'Website', 'Street', 'City', 'Country', 'PLZ', 'Season1Date', 'Season1Time', 'Season2Date', 'Season2Time', 'Image1', 'Image2', 'Image3', 'Information', 'updateTime']

        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(spot_data[i])
            setattr(self, attribute_name, attribute_value)