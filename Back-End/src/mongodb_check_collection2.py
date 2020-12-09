import pymongo
from make_dictionary import make_dictionary

def check_collection2():
    myclient = pymongo.MongoClient("mongodb+srv://administrador:go-go-ufo12345@cluster0.scjfs.mongodb.net/admin")
    mydb = myclient['mydatabase']
    collist = mydb.list_collection_names()
    if "customers" in collist:
        print("The collection exists.")
