from datetime import datetime


valor = 10
n = 1
raizes = []
def raizq(x):
    while n <= 100:
        tempo = []
        valor ** n
        n = n +1
        inicio = datetime.now().microsecond
        if(valor/2) ** 2 == valor:
            return valor/2
        else:
            if x == valor:
                x = 1
            while True:
                f = x**2 - valor 
                f_linha = 2*x
                resultado = x - (f/f_linha)
                if abs(resultado - x) <= 0.1:
                    return resultado
                else:
                    return raizq(resultado)
            
    tempo.append(abs(inicio-datetime.now().microsecond))

print()
                