import csv, sqlite3

con = sqlite3.connect("spotlist.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE spotlist (ID,SpotName,Website,OtherMedia,street,city,zip,Season1Date,Season1Time,x,y,updateTime);") # use your column names here

with open('spotlist.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['ID'],i['SpotName'],i['Website'],i['OtherMedia'],i['street'],i['city'],i['zip'],i['Season1Date'],i['Season1Time'],i['x'],i['y'],i['updateTime']) for i in dr]

cur.executemany("INSERT INTO spotlist (ID,SpotName,Website,OtherMedia,street,city,zip,Season1Date,Season1Time,x,y,updateTime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()

#FMID,MarketName,Website,Facebook,Twitter,Youtube,OtherMedia,street,city,County,State,zip,Season1Date,Season1Time,Season2Date,Season2Time,Season3Date,Season3Time,Season4Date,Season4Time,x,y,Location,Credit,WIC,WICcash,SFMNP,SNAP,Organic,Bakedgoods,Cheese,Crafts,Flowers,Eggs,Seafood,Herbs,Vegetables,Honey,Jams,Maple,Meat,Nursery,Nuts,Plants,Poultry,Prepared,Soap,Trees,Wine,Coffee,Beans,Fruits,Grains,Juices,Mushrooms,PetFood,Tofu,WildHarvested,updateTime
#'FMID','MarketName','Website','Facebook','Twitter','Youtube','OtherMedia','street','city','County','State','zip','Season1Date','Season1Time','Season2Date','Season2Time','Season3Date','Season3Time','Season4Date','Season4Time','x','y','Location','Credit','WIC','WICcash','SFMNP','SNAP','Organic','Bakedgoods','Cheese','Crafts','Flowers','Eggs','Seafood','Herbs','Vegetables','Honey','Jams','Maple','Meat','Nursery','Nuts','Plants','Poultry','Prepared','Soap','Trees','Wine','Coffee','Beans','Fruits','Grains','Juices','Mushrooms','PetFood','Tofu','WildHarvested','updateTime'
#i['County'],