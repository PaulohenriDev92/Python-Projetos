from datetime import date
ano_atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range (1, 8):
    nasc = int (input(f'Em que ano a {pessoa}ª pessoa nasceu ? '))
    idade = ano_atual - nasc
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'A todo tivemos {totalmaior} pessoas MAIORES de idade')
print(f'E também tivemos {totalmenor} pessoas menores de idade')