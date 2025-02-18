#dez numeros em ordem inversa.
#sum: Faz a media das notas
#len: soma todos os elementos da lista
lista = []
for x in range(4):
    num = float(input(f"Digite a {x + 1}º nota:  "))
    lista.append(num)
media = sum(lista)/len(lista)
print(media)