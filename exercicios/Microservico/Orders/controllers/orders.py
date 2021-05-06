from Orders.DataBase import orders_bd

def listar_pedidos(dados):       
    try:
        return orders_bd.consultar(dados)
    except Exception as error:
        return dict(Status=400, Text=str(error))  

def cadastrar_pedidos(dados):       
    try:
        return orders_bd.cadastrar(dados)
    except Exception as error:
        return dict(Status=400, Text=str(error))                        

def atualizar_pedidos(dados):       
    try:
        return orders_bd.atualizar(dados)
    except Exception as error:
        return dict(Status=400, Text=str(error))                        

def deletar_pedidos(id):       
    try:
        return orders_bd.deletar(id)
    except Exception as error:
        return dict(Status=400, Text=str(error))                

def limpar_pedidos():
    try:
        return orders_bd.limpar()
    except Exception as error:
        return dict(Status=400, Text=str(error))        