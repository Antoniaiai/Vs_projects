# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

par = []
impar = []
for x in range(20):
    numero = int(input(f"Digite o {x + 1}º número: "))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(f"Os números pares foram: {par}")
print(f"Os números impares foram: {impar}")