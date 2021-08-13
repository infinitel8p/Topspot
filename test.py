headers = ['id', 'SpotName', 'x', 'y', 'MapsLink', 'Website', 'Street', 'City', 'Country', 'PLZ', 'Season1Date', 'Season1Time', 'Season2Date', 'Season2Time', 'Image1', 'Image2', 'Image3', 'Information', 'updateTime']

for i in range(len(headers)):
    attribute_name = headers[i]
    attribute_value = str(spot_data[i])
    setattr(attribute_name, attribute_value)
print(id)
print(x)
print(y)
print(SpotName)