from time import sleep
from random import randint

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
print('{:-^40}'.format('JOGO DA PEDRA PAPEL & TESOURA'))
jogador = int (input('Qual sua jogada: '))
print('')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.5)
print('')
print('-=-' * 11)
computador = randint (0, 2)
print(f'O jogador jogou {opcoes[jogador]}')
print(f'O computador jogou {opcoes[computador]}')
print('-=-' * 11)
if computador == 0:     #COMPUTADOR JOGA PEDRA
    if jogador == 0:
        print('Resultado: EMPATE')
    elif jogador == 1:
        print('Resultado: JOGADOR VENCE')
    elif jogador == 2:
        print('Resultado: COMPUTADOR VENCE')
    else:
        print('OPÇÃO INVÁLIDA')

elif computador == 1:   #COMPUTADOR JOGA PAPEL
    if jogador == 0:
        print('Resultado: COMPUTADOR VENCE')
    elif jogador == 1:
        print('Resultado: EMPATE')
    elif jogador == 2:
        print('Resultado: JOGADOR VENCE')
    else:
        print('OPÇÃO INVÁLIDA')

elif computador == 2:   #COMPUTADOR JOGA TESOURA
    if jogador == 0:
        print('Resultado: JOGADOR VENCE')
    elif jogador == 1:
        print('Resultado: COMPUTADOR VENCE')
    elif jogador == 2:
        print('Resultado: EMPATE')
    else:
        print('OPÇÃO INVÁLIDA')



