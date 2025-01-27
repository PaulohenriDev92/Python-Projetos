print('-=-' * 5, 'SAIBA SEU IMC - ÍNDICE DE MASSA CORPORAL', '-=-' * 5)
peso = float (input('Peso (Kg): '))
alt = float (input('Altura (m): '))
iMC = peso / (alt ** 2)
print(f'Seu IMC é: {iMC:.1f}')
if iMC < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= iMC < 25:
    print('Peso Normal')
elif 25 <= iMC < 30:
    print('Sobrepeso')
elif 30 <= iMC < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')