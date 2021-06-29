# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="T0day@1234",
#   database="mysqlpolicy"
# )

# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#      print(x)


import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['anju']
#print(mydb.list_collection_names())
mycol = mydb['livai_booking']

for x in mycol.find():
  print(x)

  






