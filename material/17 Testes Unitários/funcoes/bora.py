from builtins import TypeError


def soma(n1, n2):
    return n1 + n2

def raiz(n1):

    if not isinstance(n1, int):
        raise TypeError
    elif n1 < 0:
        raise ValueError

    return n1 ** 0.5


def add(n):
    return n + 1