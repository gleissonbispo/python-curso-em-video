print('{:$^40}'.format(' Conversor de Moedas '))

dinheiro = float(input('Quantos Reais você tem na carteira?'))
dolar = (dinheiro / 5)

print(f'\nCom R$ {dinheiro:.2f}, você pode comprar US$ {dolar:.2f}!')