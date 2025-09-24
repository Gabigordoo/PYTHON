from collections.abc import Callable

Soma_Tipos = Callable[[int, int], int]

def executa(func: Soma_Tipos, a: int, b: int) -> int:
    return func(a, b)


def soma(x: int, y: int) -> int:
    return x + y

print(executa(soma, 10, 5))