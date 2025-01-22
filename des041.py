from datetime import date
ano_nasc = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'Ele tem {idade} anos.')
atleta_m = 9
atleta_i = 14
atleta_j = 19
atleta_s = 20
if idade <= atleta_m:
    tempo_falta = atleta_i - idade
    print(f'CLASSIFICADO: MIRIM \nFalta {tempo_falta} para se tornar categoria INFANTIL.')
elif idade <= atleta_i:
    tempo_falta = atleta_j - idade
    print(f'CLASSIFICADO: INFANTIL \nFalta {tempo_falta} para se tornar CATEGORIA JUNIOR ')
elif idade <= atleta_j:
    tempo_falta = atleta_s - idade
    print(f'CLASSIFICADO: JUNIOR \nFalta {tempo_falta} para se tornar CATEGORIA SÊNIOR ')
elif idade <= atleta_s:
    print('CLASSIFICADO: SÊNIOR \nÉ necessário ter mais de 20 anos para CATEGORIA MASTER')
else:
    print('CLASSIFICADO: MASTER')