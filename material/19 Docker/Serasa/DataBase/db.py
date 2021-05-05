DB_NAME = "score_db"
DB_HOST = "master"
DB_PORT = 3306
DB_USER = "root"


import MySQLdb
try:
    conn = MySQLdb.connect(db=DB_NAME, host=DB_HOST, port=DB_PORT, user=DB_USER)
    conn.autocommit(True)
    cursor = conn.cursor()
except MySQLdb.OperationalError as error:
    print("Erro: " + error.args[1])
