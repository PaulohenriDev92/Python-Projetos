print('=' * 43)
print(' ' * 8 ,'10 TERMOS DE UMA RAZÃO')
print('=' * 43)
p_t = int (input('Primeiro termo: '))
r = int (input('Razão: '))
decimo = p_t + (10 - 1) * r
for c in range (p_t, decimo + r , r):
    print(f'{c}', end=' ')
print('ACABOU')