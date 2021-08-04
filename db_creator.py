import pandas

data = pandas.read_csv(r"spotlist.csv")
df = pandas.DataFrame(data, columns=['ID','SpotName','Website','OtherMedia','street','city','County','zip','Season1Date','Season1Time','x','y','updateTime'])
df.to_sql("spotlist", con="sqlite:///spotlist.db", if_exists='append')

#https://datatofish.com/import-csv-sql-server-python/