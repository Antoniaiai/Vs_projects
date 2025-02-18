#i = variavel contador
#range = loop
#lista.append: adiciona os numeros na lista

while True:
    lista = []

    for i in range(5):#parametros de repetição
        num = int(input(f"digite o {i + 1}º número: "))
        lista.append(num)
    print(lista)
    refazer = input("Deseja refazer? (s/n): ").lower()
    if refazer != 's':
        print("Programa encerrado. Obrigado!")
        break