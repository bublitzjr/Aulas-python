class CadastroError(Exception):
    pass


class CpfNaoNumerico(CadastroError):
    pass


class CpfNaoExistente(CadastroError):
    pass


class CpfTamanhoInvalido(CadastroError):
    pass


def verifica_cpf(cpf: str):
    if not len(cpf) == 11:
        raise CpfTamanhoInvalido("mg")

    # if cpf not in banco_dados:
    #     raise CpfNaoExistente()

    if not cpf.isdigit():
        raise CpfNaoNumerico


try:
    cpf = input("Cpf: ")
    verifica_cpf(cpf)
    print("Passou pela verificação")
except CpfTamanhoInvalido:
    print("Tamanho errado")
except CpfNaoNumerico:
    print("Não numerico")






