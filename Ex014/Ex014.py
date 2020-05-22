print('{:-^30}'.format(' Conversor de Temperatura '))

cel = float(input('Digite a temperatura em Celsius: '))
#formula para conversão: F=1,8C+32
far = ((1.8 * cel) + 32)

print(f'\nA temperatura de {cel:.2f}°C equivale a {far:.2f}°F')
