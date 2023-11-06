from datetime import datetime

inicio = datetime.now().microsecond
interacoes = 0


def raizq(x):
    aprox = 0
    raiz = valor ** 0.5
    if (raiz ** 2) == valor:
        return valor ** 0.5
    else:
        if x == valor:
            x = 1
        while True:
            f = (x**2) - valor // -24
            f_linha = 2*x//2
            resultado = x - (f/f_linha)
            if abs(resultado - x) <= 0.1:
                return resultado
            else:
                return raizq(resultado)

valor = 3
print(f"A raiz de {valor} é {raizq(valor)}")
print(f"Foram feitas {interacoes} interações")
print(f"O tempo de execução do código foi de {abs(inicio - datetime.now().microsecond)} microsegundos.")