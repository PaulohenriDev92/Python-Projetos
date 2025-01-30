from time import sleep
from emoji import emojize
print('CONTAGEM FOGOS DE ARTIFÍCIOS'.center(40, '-'))

for c in range (10, -1, -1): #DECREMENTANDO DE 1 EM 1 (10,9,8,...,1.)
    sleep(1)
    print(c)
print('')
print(emojize('FOGO !!! :collision: :collision: :collision:'))