import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017")
# print(conn.list_database_names())

db = conn["Mongo"]
# print(db.list_collection_names())
usuario = db["usuarios"]

pessoa = dict(nome="teste", dados=dict(cpf="0000", idade=40, altura=10))
# pessoa2 = dict(nome="teste", idade=13)
usuario.insert_one(pessoa)
# usuario.insert_many([pessoa, pessoa2])

filtro = {"dados":{"cpf":"0000"}}
for i in usuario.find(filtro):
    print(i)