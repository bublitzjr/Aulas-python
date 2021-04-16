import conexaoBD

class Pessoas:

    def __init__(self, nome="", cpf="", idade=0, altura=0):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.altura = altura
        self.cursor = conexaoBD.conn.cursor()

    def persistir_no_banco(self, sql) -> bool:
        if self.cursor.execute(sql) > 0:
            conexaoBD.conn.commit()
            return True
        else:
            return False

    def pesquisar_pessoa(self, nome):
        sql = f"SELECT * from exemplotabela WHERE nome LIKE '%{nome}%'"
        cursor = conexaoBD.conn.cursor()
        cursor.execute(sql)

        print(f"\n{' LISTA DE PESQUISA ':=^60}")
        print(f"{'ID':<4}\t{'Nome':<15}\t{'CPF':<15}\t{'Idade':<8}\t{'Altura':<10}")
        print(f"{'':-^60}")
        if cursor.rowcount != 0:
            for i in cursor.fetchall():
                print(f"{i[1]:<4}\t{i[0]:<15}\t{i[2]:<15}\t{i[3]:<8}\t{i[4]:<10}")
        else:
            print(f"{'Pessoa não foi encontrada :(': ^60}")
        print(f"{'':=^60}")

    def listar_todos(self):
        sql = f"SELECT * from exemplotabela"
        cursor = conexaoBD.conn.cursor()
        cursor.execute(sql)

        print(f"\n{' LISTA DE PESSOAS ':=^60}")
        print(f"{'ID':<4}\t{'Nome':<15}\t{'CPF':<15}\t{'Idade':<8}\t{'Altura':<10}")
        print(f"{'':-^60}")
        if cursor.rowcount != 0:
            for i in cursor.fetchall():
                print(f"{i[1]:<4}\t{i[0]:<15}\t{i[2]:<15}\t{i[3]:<8}\t{i[4]:<10}")
        else:
            print(f"{'Lista vazia :(': ^60}")
        print(f"{'':=^60}")

    def inserir_pessoa(self):
        sql = f"INSERT INTO exemplotabela (Nome, CPF, idade, altura) " \
              f"VALUES ('{self.nome}', '{self.cpf}', '{self.idade}', '{self.altura}')"
        self.persistir_no_banco(sql)

    def deleter_pessoa(self, cpf_pessoa):
        sql = f"DELETE FROM exemplotabela WHERE CPF = '{cpf_pessoa}'"
        existe = self.persistir_no_banco(sql)

        if existe == False:
            raise Exception("Não encontrado !")

    def deletar_todos(self):
        sql = f"DELETE FROM exemplotabela"
        self.persistir_no_banco(sql)

    def atualizar_dados_pessoa(self, id, dados_pessoa):
        campos = []
        campos_alter = ""
        sql = f" UPDATE exemplotabela SET "

        if dados_pessoa['nome'] != "":
            campos.append("nome")
        if dados_pessoa['cpf'] != "":
            campos.append("cpf")
        if dados_pessoa['idade'] != "":
            campos.append("idade")
        if dados_pessoa['altura'] != "":
            campos.append("altura")

        for i in campos:
            if i == "nome":
                campos_alter += f" Nome = '{dados_pessoa['nome']}', "
            if i == "CPF":
                campos_alter += f" CPF = '{dados_pessoa['cpf']}', "
            if i == "idade":
                campos_alter += f" idade = {dados_pessoa['idade']}, "
            if i == "altura":
                campos_alter += f" altura = {dados_pessoa['altura']} "

        sql += campos_alter
        sql += f"WHERE id = {id}"
        existe = self.persistir_no_banco(sql)

        if existe == False:
            raise Exception("Não encontrado !")

