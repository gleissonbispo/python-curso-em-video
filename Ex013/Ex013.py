print('{:=^30}'.format(' Calculadora de Aumentos '))

salario = float(input('Digite o salário do funcionário para saber o aumento:'))
salarioaumento = salario + (salario * (15 / 100))

print(f"""\nO salário atual do funcionário é de R$ {salario:.2f}
Com o aumento de 15% o novo salário passa a ser R$ {salarioaumento:.2f}""")
