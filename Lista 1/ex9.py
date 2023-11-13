from datetime import datetime


resultado = []
tempo_total = []

def raizq(x):
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
                
                

for i in range(1,101):
    valor = 10 ** i

    inicio = datetime.now().microsecond
    res_raiz = raizq(valor)
    fim = datetime.now().microsecond
    
    tempo = abs(inicio-fim)
    tempo_total.append(tempo)
    resultado.append(res_raiz)

    print(f"A raiz de {valor} é aproximadamente {res_raiz:.2f}")
    print(f"O tempo de execução desde {i}º código foi de {tempo} microsegundos")

print(f"Os resultados das raizes são: {resultado}")
print(f"O tempo total das execuções em ordem foi {tempo_total}")