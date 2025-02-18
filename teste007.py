# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
# QUE RAIIIIVAAAAA VAI TOMAR NO CU CODIGO BUCETA, ODEIO LISTA VAI SE FODERRRR TWO DAYS IN THE SAME SHITT FUCK U MARK ZUCKEMBERG
notas_aluno = []
nomes = []
#listas vazia para ir adicionando

for x in range(10):
    nome = input(f"Digite o nome do {x + 1}° aluno: ")
    nomes.append(nome)
    #loop que add o nome do aluno à lista
    
    soma_notas = 0

    for y in range(4):
        while True:  # Validação para garantir que a nota seja entre 0 e 10
            try:
                nota = float(input(f"Digite a {y + 1}º nota de {nome}: "))
                if 0 <= nota <= 10:
                    soma_notas += nota
                    break  # Se a nota for válida, sai do loop
                else:
                    print("Nota inválida! A nota deve ser entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Valor inválido! Por favor, insira um número.")
    
    media = soma_notas/4
    notas_aluno.append(media)

aprovados = 0
print("Alunos aprovados:")
for i in range(10):
    if notas_aluno[i] >= 7.0:
        print(f"- {nomes[i]} com média {notas_aluno[i]}")
        aprovados += 1

# Exibição do total de aprovados
print(f"Número total de alunos com média maior ou igual a 7.0: {aprovados}")