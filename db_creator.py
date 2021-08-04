import pandas

data = pandas.read_csv(r"spotlist.csv")
df = pandas.DataFrame(data, columns=['FMID','MarketName','Website','Facebook','Twitter','Youtube','OtherMedia','street','city','County','State','zip','Season1Date','Season1Time','Season2Date','Season2Time','Season3Date','Season3Time','Season4Date','Season4Time','x','y','Location','Credit','WIC','WICcash','SFMNP','SNAP','Organic','Bakedgoods','Cheese','Crafts','Flowers','Eggs','Seafood','Herbs','Vegetables','Honey','Jams','Maple','Meat','Nursery','Nuts','Plants','Poultry','Prepared','Soap','Trees','Wine','Coffee','Beans','Fruits','Grains','Juices','Mushrooms','PetFood','Tofu','WildHarvested','updateTime'])
print(df.to_sql("spotlist", con="sqlite:///spotlist.db", if_exists='append'))

#https://datatofish.com/import-csv-sql-server-python/