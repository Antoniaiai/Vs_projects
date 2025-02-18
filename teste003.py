#dez numeros em ordem inversa.

lista = []
for x in range(10):
    num = int(input(f"Digite o {x + 1}º número:  "))
    lista.append(num)

for num in reversed(lista):
    print(num)