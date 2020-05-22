from math import cos, sin, tan, radians

ang = float(input('Digite um ângulo: '))

cs = cos(radians(ang))
sn = sin(radians(ang))
tg = tan(radians(ang))

print(f"""\nVocê digitou o ângulo {ang:.2f}°
O cosseno deste ângulo vale: {cs:.2f}
O seno deste ângulo vale: {sn:.2f}
A tangente deste ângulo vale: {tg:.2f}""")