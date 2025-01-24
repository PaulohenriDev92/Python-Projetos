print('-=-' * 5, 'DESCUBRA SE O TRIIÂNGULO É EQUILÁTERO, ISÓSCELES ou ESCALENO', '-=-'* 5)
lado1 = float (input('Primeiro seguimento: '))
lado2 = float (input('Segundo seguimento: '))
lado3 = float (input('Terceiro seguimento: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os seguimentos acima podem formar um triangulo ', end = '')
    if lado1 == lado2 == lado3:
        print('Triângulo EQUILÁTERO')
    elif lado1 != lado2 != lado3 != lado1:
        print('Triângulo ESCALENO')
    else:
        print('Triângulo ISÓSCELES')
else:
    print('Os seguimentos acima não formam um TRIÂNGULO')
