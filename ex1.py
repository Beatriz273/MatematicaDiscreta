n = int(input("Insira um valor final para a contagem de números naturais: "))
cont = 0
v = []

for i in range(1, n+1):
    cont = 0
    if n % i == 0:
        v.append(i)
        cont += 1
    if cont == 0:
        print(f"{n} é primo")

print(f"Os números que {n} é divisível são {v}")
    