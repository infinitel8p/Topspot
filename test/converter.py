import csv, sqlite3

con = sqlite3.connect("spotlist.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE spotlist (FMID,MarketName,Website,Facebook,Twitter,Youtube,OtherMedia,street,city,County,State,zip,Season1Date,Season1Time,Season2Date,Season2Time,Season3Date,Season3Time,Season4Date,Season4Time,x,y,Location,Credit,WIC,WICcash,SFMNP,SNAP,Organic,Bakedgoods,Cheese,Crafts,Flowers,Eggs,Seafood,Herbs,Vegetables,Honey,Jams,Maple,Meat,Nursery,Nuts,Plants,Poultry,Prepared,Soap,Trees,Wine,Coffee,Beans,Fruits,Grains,Juices,Mushrooms,PetFood,Tofu,WildHarvested,updateTime);") # use your column names here

with open('spotlist.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin, delimiter=';') # comma is default delimiter
    to_db = [(i['FMID'],i['MarketName'],i['Website'],i['Facebook'],i['Twitter'],i['Youtube'],i['OtherMedia'],i['street'],i['city'],i['County'],i['State'],i['zip'],i['Season1Date'],i['Season1Time'],i['Season2Date'],i['Season2Time'],i['Season3Date'],i['Season3Time'],i['Season4Date'],i['Season4Time'],i['x'],i['y'],i['Location'],i['Credit'],i['WIC'],i['WICcash'],i['SFMNP'],i['SNAP'],i['Organic'],i['Bakedgoods'],i['Cheese'],i['Crafts'],i['Flowers'],i['Eggs'],i['Seafood'],i['Herbs'],i['Vegetables'],i['Honey'],i['Jams'],i['Maple'],i['Meat'],i['Nursery'],i['Nuts'],i['Plants'],i['Poultry'],i['Prepared'],i['Soap'],i['Trees'],i['Wine'],i['Coffee'],i['Beans'],i['Fruits'],i['Grains'],i['Juices'],i['Mushrooms'],i['PetFood'],i['Tofu'],i['WildHarvested'],i['updateTime']) for i in dr]

cur.executemany("INSERT INTO spotlist (FMID,MarketName,Website,Facebook,Twitter,Youtube,OtherMedia,street,city,County,State,zip,Season1Date,Season1Time,Season2Date,Season2Time,Season3Date,Season3Time,Season4Date,Season4Time,x,y,Location,Credit,WIC,WICcash,SFMNP,SNAP,Organic,Bakedgoods,Cheese,Crafts,Flowers,Eggs,Seafood,Herbs,Vegetables,Honey,Jams,Maple,Meat,Nursery,Nuts,Plants,Poultry,Prepared,Soap,Trees,Wine,Coffee,Beans,Fruits,Grains,Juices,Mushrooms,PetFood,Tofu,WildHarvested,updateTime) VALUES (?, ?);", to_db)
con.commit()
con.close()

#'FMID','MarketName','Website','Facebook','Twitter','Youtube','OtherMedia','street','city','County','State','zip','Season1Date','Season1Time','Season2Date','Season2Time','Season3Date','Season3Time','Season4Date','Season4Time','x','y','Location','Credit','WIC','WICcash','SFMNP','SNAP','Organic','Bakedgoods','Cheese','Crafts','Flowers','Eggs','Seafood','Herbs','Vegetables','Honey','Jams','Maple','Meat','Nursery','Nuts','Plants','Poultry','Prepared','Soap','Trees','Wine','Coffee','Beans','Fruits','Grains','Juices','Mushrooms','PetFood','Tofu','WildHarvested','updateTime'