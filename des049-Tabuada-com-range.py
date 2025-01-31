print(' TABUADA ELETRÔNICA '.center(50, '='))
print('')
num = int (input('Qual valor deseja saber na Tabuada ? '))
print('')
for i in range (1, 11):
    mult = num * i
    print(f'{num} x {i} = {mult}')