# import pymongo
# from bson.objectid import ObjectId
#
# conn = pymongo.MongoClient("mongodb://localhost:27017/")

# print(conn.list_database_names())

# db = conn["Llama"]
# usuarios = db["usuarios"]

# pessoa = dict(nome="Teste", dados=dict(cpf="0000", idade=15, altura=1.8))
# usuarios.insert_one(pessoa)

# usuarios.delete_one({"dados": {"cpf": "0000", "idade":15, "altura":1.8}})

# filtro = dict(nome="A")
# novos_valores = dict(nome="Letra A")
# usuarios.update_one(filtro, {"$set": novos_valores})

# import pandas as pd

# print(pd.DataFrame(usuarios.find()))

# # Criando id com 12 digitos
# print(ObjectId(b'abcdefghijkl'))
#
# # Criando id com 24 digitos
# print(ObjectId('0123456789ab0123456789ab'))

# for i in usuarios.find({}, {"_id": 0, "nome": 1}):
#     print(i)
