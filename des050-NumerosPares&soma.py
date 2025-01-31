cont = 0
soma = 0
for c in range (1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'A quantidade de números PARES são: {cont}  e soma é: {soma}')