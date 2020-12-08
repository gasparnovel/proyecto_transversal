def make_db():
    myclient = pymongo.MongoClient("mongodb+srv://administrador:go-go-ufo12345@cluster0.scjfs.mongodb.net/admin")
    mydb = myclient["mydatabase"]
    
    mycol = mydb["customers"]

    mylist = make_dictionary

    x = mycol.insert_many(mylist)

    #print list of the _id values of the inserted documents:
    print(x.inserted_ids)

def verification():
    collist = mydb.list_collection_names()
        if "customers" in collist:
    print("The collection exists.")