print('{:=^30}'.format(' Calculo de KM '))

km = float(input('Quantos KMs foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
valor = (dias * 60) + (km * 0.15)

print(f"""\nComo você andou {km} KM e alugou o carro por {dias} dias
O total a se pagar pelo serviço é R$ {valor:.2f}""")