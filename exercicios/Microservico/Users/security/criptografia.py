import base64

def codificar_dado(dado):
    ascii_dado = dado.encode('ascii')
    dado_codificado_ascii = base64.b64encode(ascii_dado)    
    dado_codificado = dado_codificado_ascii.decode('ascii')

    return dado_codificado

def decodificar_dado(dado):    
    dado_codificado_ascii = dado.encode('ascii')  
    dado_decodificado_ascii = base64.b64decode(dado_codificado_ascii)  
    dado_decodificado = dado_decodificado_ascii.decode('ascii')
    
    return dado_decodificado