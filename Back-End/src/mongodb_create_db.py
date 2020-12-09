import pymongo
from make_dictionary import make_dictionary
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson.errors import InvalidId
# Conexion con la base de datos
# replace "uri" with your Atlas URI string - should look like mongodb+srv://...
uri = "mongodb+srv://administrador:go-go-ufo12345@cluster0.scjfs.mongodb.net/admin"
client = pymongo.MongoClient(uri)
# seleccionamos la bbdd sample_mflix
ufo = client.ufo
# seleccionamos la coleccion users
naves = ufo.naves
print(dumps(naves.find_one(make_dictionary), indent=2))