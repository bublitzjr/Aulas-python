from Users.DataBase import usuarios_bd

def listar_usuario(cpf):
    try:
        return usuarios_bd.consultar(cpf)
    except Exception as error:
        return dict(Status=400, Text=str(error))                        

def cadastrar_usuarios(dados):    
    try:
        return usuarios_bd.cadastrar(dados)
    except Exception as error:
        return dict(Status=400, Text=str(error))                        

def atualizar_usuarios(dados):
    try:
        return usuarios_bd.atualizar(dados)
    except Exception as error:
        return dict(Status=400, Text=str(error))                        

def deletar_usuarios(dados):
    try:
        return usuarios_bd.deletar(dados)
    except Exception as error:
        return dict(Status=400, Text=str(error))       

def limpar_usuarios():
    try:
        return usuarios_bd.limpar()
    except Exception as error:
        return dict(Status=400, Text=str(error))       


