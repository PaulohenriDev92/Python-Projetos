frase = str (input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print(junto)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto}, temos {inverso}')
if inverso == junto:
    print('Temos um PALÍNDROMO')
else:
    print('NÃO temos um PALÍNDROMO')