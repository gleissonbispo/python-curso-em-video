print('{:#^40}'.format(' Medidor de Tinta '))

altura = float(input('Qual a alura da sua parede?'))
largura = float(float(input('Qual a altura da sua parede?')))

m2 = altura * largura
tinta = m2 / 2

print(f"""\nSua parede tem {altura:.2f}m de altura e {largura:.2f}m de largura totalizando {m2:.2f}m2
Dessa forma serão necessários {tinta:.2f} litros de tinta para pintá-la""")