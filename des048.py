soma = 0
cont = 0
for numero in range (1, 501, 2):
    if numero % 3 == 0:
        cont += 1 # cont = cont + 1     # Nesta linha refere-se a um CONTADOR, soma 1
        soma += numero #  soma = soma + numero      # Nesta linha refere-se a um ACUMULADOR
print(f'A soma de todos os {cont} valores solicitados é: {soma}')