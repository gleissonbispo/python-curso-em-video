print('{:=^40}'.format('Conversor de Medidas'))

medida = float(input('\n Digite a medida em metros a ser convertida:'))
cent = medida * 100
mili = medida * 1000

print(f'\n {medida:.2f} metros equivalem a {cent:.2f} centímetros e {mili:.2f} milímetros!')
