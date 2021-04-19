import MySQLdb

class Hotel:

    conn = MySQLdb.connect(db="Hoteis", user="root", host="localhost", port=3306)

    def __init__(self, cidade):
        self.cidade = cidade
        self.cursor = self.conn.cursor()

        self.sql = f"""select a.id_hotel, a.nome_hotel,a.classificacao, a.preco_diaria, a.academia, a.pisicina, a.refeicoes, a.vagas, b.nome_cidade, c.nome_estado from hoteis a 
                            join cidades b on b.id_cidade = a.fkcidade
                            join estados c on b.fkEstado = c.id_estado"""
        self.where = ""

    def lista_hoteis(self):
        possui_academia, possui_piscina, oferece_refeicao  = "Não", "Não", "Não"
        print(f"\n{' LISTA DE HOTEIS ':=^120}")
        print(
            f"{'ID':<2}\t{'Nome':<15}\t{'Stars':<5}\t{'Preço':<8}\t{'Academia':<8}\t{'Piscina':<8}\t{'Refeições':<10}"
            f"\t{'Vagas':<10}\t{'Cidade':<10}\t{'Estado':<10}\t")
        for i in self.cursor:
            if i[4] == 1: possui_academia = "Sim"
            if i[5] == 1: possui_piscina = "Sim"
            if i[6] == 1: oferece_refeicao = "Sim"
            print(
                f"{i[0]:<2}\t{i[1]:<15}\t{i[2]:<5}\t{i[3]:<8}\t{possui_academia:<8}\t{possui_piscina:<8}"
                f"\t{oferece_refeicao:<10}\t{i[7]:<10}\t{i[8]:<10}\t{i[9]:<10}\t")

    def filtro_por_academia(self):
        self.where += f"""
                        and a.academia = 1 
                        """

    def filtro_por_piscina(self):
        self.where += f"""
                        and a.pisicina = 1 
                        """

    def filtro_por_preco(self, valor_minimo, valor_maximo):
        self.where += f"""
                        and a.preco_diaria >= {valor_minimo} 
                        and a.preco_diaria <= {valor_maximo}
                        """

    def filtro_por_estrelas(self, estrela):
        self.where += f"""
                        and a.classificacao = {estrela}
                        """

    def filtro_por_refeicoes(self):
        self.where += f"""
                        and a.classificacao = 1
                        """

    def filtro_vagas(self):
        self.where += f"""
                        and a.vagas > 0
                        """

    def consultar_por_cidade(self):
        regiao = self.pega_regiao()
        self.where = f"""
                     where b.regiao = '{regiao}'                    
                    """

    def pega_regiao(self):
        sql = f"""select a.regiao from cidades a
                where a.nome_cidade = '{self.cidade}'
                 """
        self.cursor.execute(sql)

        for i in self.cursor:
            regiao = i[0]

            return regiao

    def filtrar(self):
        self.sql += self.where
        self.cursor.execute(self.sql)
        self.lista_hoteis()

a = Hotel("blumenau")
try:
    a.consultar_por_cidade()
    # a.filtro_por_academia()
    a.filtro_por_preco(50, 3000)
    a.filtro_por_estrelas(3)
    a.filtrar()
except Exception as e:
    print(e)


# a.filtro_vagas()

