import MySQLdb

conn = MySQLdb.connect(db="Llama", user="root", host="localhost", port=3306)
cursor = conn.cursor()


# cursor.execute("select * from aqui")
# cursor.fetchall()
# for col in cursor.description:
#     print(col[0])

# ///////////////////////////////////////////////////////////////

# nome = "AAA"
# cpf = "353"
#
# sql = f"INSERT INTO aqui VALUES ('{nome}', DEFAULT, '{cpf}')"
# cursor.execute(sql)
#
# conn.commit()

# ///////////////////////////////////////////////////////////////

# nome = input("Digite seu nome: ")
# sql = f"""
#       Update aqui
#       Set Nome = '{nome}'
#       where cpf = '002'
#       """
#
# cursor.execute(sql)
# conn.commit()

# ///////////////////////////////////////////////////////////////

sql = f"""
      Delete from aqui
      where cpf = '65465'
      """

cursor.execute(sql)
print(conn.commit())


def delete_data(id: str):
    sql = "DELETE FROM aqui WHERE id = ?"

    cursor.execute(sql, [id])
    try:
        conn.commit()
        return True
    except:
        return False


delete_data("655554864")

