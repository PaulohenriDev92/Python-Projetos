print('{:-^40}'.format(' LOJAS PAULO & CIA '))
preco = float (input('Preço das compras: R$ '))
print('''
FORMAS DE PAGAMENTO

[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão 
''')

op = int(input('Qual opção deseja: '))
if op < 1 or op > 4:
    print('\033[32mOpção INVÁLIDA\033[m')
elif op == 1:
    total = preco - (preco * 10 / 100)
    print(f'O preço da compra é: R$ {preco:.2f}, com desconto de 10% fica de: R$ {total:.2f}')
elif op == 2:
    total = preco - (preco * 5 / 100)
    print(f'O preço da compra é: R$ {preco:.2f}, com desconto de 5% fica de: R$ {total:.2f}')
elif op == 3:
    parcela = preco / 2
    print(f'O preço da compra é: R$ {preco:.2f}, em 2x fica de: R$ {parcela:.2f} SEM JUROS')
elif op == 4:
    total = preco + (preco * 20 / 100)
    total_parcelas = int(input('Quantidade de parcelas: '))
    parcela = total / total_parcelas
    print(f'O preço da compra é de: R${preco:.2f}, parcelado em {total_parcelas}x de R$ {parcela:.2f} com JUROS')
    print(f'Sua compra de R$ {preco:.2f}, com acréscimo de 20%, ficará no valor de: R$ {total:.2f}')

