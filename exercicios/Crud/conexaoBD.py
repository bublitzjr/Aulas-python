import MySQLdb

try:
    conn = MySQLdb.connect(db="aula_bd", user="root", host="localhost", port=3306)
except Exception as e:
    print("Erro de conexão: " + str(e))


