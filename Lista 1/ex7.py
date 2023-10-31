n2 = int(input("Insira um valor para a contagem de números primos: "))
cont = 0
primo = []
total = 0


for i in range(2,n2):
    cont = 0
    for j in range (2, i):
        if (i % j) == 0:
            cont += 1
    if cont == 0:
        primo.append(i)
        total += 1

print(f"Todos os números primos: {primo}")
print(f"A quantidade de números primos: {total}")
print(f"O último número primo: {primo[-1]}")