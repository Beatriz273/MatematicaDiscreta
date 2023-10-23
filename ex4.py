# Listar todos os quadrados perfeitos

inicio = int(input("Insira o início do intervalo: "))
fim = int(input("Insira o fim do intervalo: "))
v = []

for j in range (inicio, fim+1):
    raiz = j ** 0.5
    if (raiz*2) % 2 == 0:
        v.append(j)

print(f"Os números que são quadrados perfeitos são {v}")