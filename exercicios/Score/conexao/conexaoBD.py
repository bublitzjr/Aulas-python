import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", db="aula_bd")
conn.autocommit(True)
cursor = conn.cursor()