


import pymongo
from make_dictionary import make_dictionary
from bson.objectid import ObjectId
from bson.errors import InvalidId
# Conexion con la base de datos
# replace "uri" with your Atlas URI string - should look like mongodb+srv://...
uri = "mongodb+srv://administrador:go-go-ufo12345@cluster0.scjfs.mongodb.net/admin"
client = pymongo.MongoClient(uri)

db = client['teststore']
collection = db['products']
collection.insert_many(make_dictionary)