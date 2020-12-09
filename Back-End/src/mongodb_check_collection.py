import pymongo

def check_collection():
    myclient = pymongo.MongoClient("mongodb+srv://administrador:go-go-ufo12345@cluster0.scjfs.mongodb.net/admin")
    mydb = myclient['mydatabase']
    mycol = mydb["customers"]
    print(mydb.list_collection_names())