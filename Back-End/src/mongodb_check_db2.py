import pymongo


def check_db2():
    myclient = pymongo.MongoClient("mongodb+srv://administrador:go-go-ufo12345@cluster0.scjfs.mongodb.net/admin")
    dblist = myclient.list_database_names()
    if "mydatabase" in dblist:
        print("The database exists.")