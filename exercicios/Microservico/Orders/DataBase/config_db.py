import MySQLdb

NAME_DB = "AppMicroService"
USER_DB = "root"
HOST_DB = "localhost"
PORT_DB = 3306

class Conexao_bd:
    conn = MySQLdb.connect(db=NAME_DB, user=USER_DB, host=HOST_DB, port=PORT_DB)
    conn.autocommit(True)
    cursor = conn.cursor()