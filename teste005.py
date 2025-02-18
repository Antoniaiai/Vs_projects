#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

Vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = []

for x in range(10):
    letra = input(f"Digite a {x + 1}° letra: ")
    
    if letra.isalpha() and letra not in Vogais:
        consoantes.append(letra)
    
print(f"O total de consoantes é: {len(consoantes)}")
print(f"As consoantes foram: {', '.join(consoantes)}")

    