print('{:=^30}'.format(' Calculadora de Descontos '))

valor = float(input('Digite um valor para saber o desconto: '))
valordesconto = valor - (valor * (5 / 100))

print(f"""\nVocê digitou o valor: {valor:.2f}
O novo valor com desconto de 5% é de {valordesconto:.2f}""")
