print('{:=^30}'.format('Calculadora de Média'))

nota1 = float(input('\nDigite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = ((nota1 + nota2) / 2)

print(f'\nA média entre {nota1:.2f} e {nota2:.2f} é igual a {media:.2f}')