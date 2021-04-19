import MySQLdb

class Hotel:

    conn = MySQLdb.connect(db="Hoteis", user="root", host="localhost", port=3306)

    def __init__(self, cidade):
        self.cidade = cidade
        self.cursor = self.conn.cursor()
        self.sql = f"""select a.id_hotel, a.nome_hotel,a.classificacao, a.preco_diaria, a.academia, a.pisicina, a.refeicoes, a.vagas, b.nome_cidade, c.nome_estado, b.regiao from hoteis a 
                        join cidades b on b.id_cidade = a.fkcidade
                        join estados c on b.fkEstado = c.id_estado"""
        self.listaGlobal = []

    def executa_sql(self):
        self.cursor.execute(self.sql)

    def pega_regiao(self):
        regiao = self.filtrar_cidade()

        for i in self.cursor:
            if i[10] == regiao and i[7] != 0:
                self.listaGlobal.append(i)
        return self.listaGlobal

    def filtrar_cidade(self):
        for i in self.cursor:
            if i[8] == self.cidade:
                return i[10]

    def lista_hoteis(self):
        possui_academia, possui_piscina, oferece_refeicao  = "Não", "Não", "Não"
        print(f"\n{' LISTA DE HOTEIS ':=^120}")
        print(
            f"{'ID':<2}\t{'Nome':<20}\t{'Stars':<5}\t{'Preço':<8}\t{'Academia':<8}\t{'Piscina':<8}\t{'Refeições':<10}"
            f"\t{'Vagas':<10}\t{'Cidade':<10}\t{'Estado':<10}\t")
        for i in self.listaGlobal:
            if i[4] == 1: possui_academia = "Sim"
            if i[5] == 1: possui_piscina = "Sim"
            if i[6] == 1: oferece_refeicao = "Sim"
            print(
                f"{i[0]:<2}\t{i[1]:<20}\t{i[2]:<5}\t{i[3]:<8}\t{possui_academia:<8}\t{possui_piscina:<8}"
                f"\t{oferece_refeicao:<10}\t{i[7]:<10}\t{i[8]:<10}\t{i[9]:<10}\t")

    def filtro_por_academia(self):
        lista = []
        for i in self.listaGlobal:
            if i[4] == 1:
                self.listaGlobal.append(i)
        self.lista_hoteis(lista)

    def filtro_por_pisicina(self):
        lista = []
        for i in self.listaGlobal:
            if i[5] == 1:
                self.listaGlobal.append(i)
        self.lista_hoteis(lista)

    def filtro_por_preco(self, preco_minimo, preco_maximo):
        lista = []
        for i in self.listaGlobal:
            if preco_minimo <= i[3] <= preco_maximo:
                self.listaGlobal.append(i)
        self.lista_hoteis(lista)

    def filtro_refeicao(self, lista_hoteis):
        lista = []
        for i in lista_hoteis:
            if i[6] == 1:
                self.listaGlobalself.listaGlobal.append(i)
        # self.lista_hoteis(lista)



teste = Hotel("Blumenau")
teste.executa_sql()
# teste.lista_hoteis()
teste.pega_regiao()
teste.filtro_por_academia()
teste.lista_hoteis()
# teste.filtrar_cidade()
# teste.filtro_por_academia()
# teste.lista_hoteis()
# teste.filtro_por_pisicina(lista)
# teste.filtro_por_preco(50, 100, lista)
# teste.filtro_refeicao(lista)