import MySQLdb

conn = MySQLdb.connect(db="aula_bd", user="root", host="localhost", port=3306)
cursor = conn.cursor()

# cursor.execute("select * from exemplotabela")
# for i in cursor.fetchall(): # Printando valores
#     print(i)

# cursor.fetchall()
# print(cursor.description)

# for col in cursor.description: Pegando nome da coluna
#     print(col[0])

# nome = "Jefferson"
# cpf = "123"
# cursor.execute(f"INSERT INTO exemplotabela (Nome, CPF) VALUES ('{nome}', '{cpf}');")
# conn.commit()


# nome = "BLA"
# cpf = "123"
# sql = f"update exemplotabela set Nome = '{nome}' where CPF = '{cpf}'"
# cursor.execute(sql)
# conn.commit()

sql = f"delete from exemplotabela where id = 10"
cursor.execute(sql)
conn.commit()




