from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hyp = hypot(co, ca)

print(f'\nPara o CO {co:.3f} e CA {ca:.3f} a Hypotenusa vale {hyp:.3f}')
