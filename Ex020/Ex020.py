from random import shuffle

print('{:=^40}'.format(' Sorteador de Alunos '))

a1 = input('Escreva o nome do 1° aluno: ')
a2 = input('Escreva o nome do 2° aluno: ')
a3 = input('Escreva o nome do 3° aluno: ')
a4 = input('Escreva o nome do 4° aluno: ')
escolha = [a1, a2, a3, a4]
shuffle(escolha)

print(f'O escolhda para os alunos foi {escolha}!')