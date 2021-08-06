from kivymd.uix.dialog import ListMDDialog

class LocationPopupMenu(ListMDDialog):
    def __init__(self, spot_data):
        super().__init__()

        headers = "SpotName", "x", "y", "MapsLink", "Website", "Street", "City", "Country", "PLZ", "Season1_date", "Season1_hours", "Season2_date", "Season2_hours", "Images", "Information"
        headers = headers.split(",")

        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = spot_data[i]
            setattr(self, attribute_name, attribute_value)