#10 numeros e imprimir

while True:
    lista = []

    for x in range(10):
        num= int(input(f"Digite o {x + 1}º número: "))
        lista.append(num)
    print(lista)
    loop = input("Deseja continuar? S/n: ").lower(loop)
    if loop != 'S':
        print("Programa encerrado.")
        break