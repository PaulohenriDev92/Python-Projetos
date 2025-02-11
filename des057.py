sexo = str (input('Digite seu sexo: ')).upper()[0].strip()
while sexo not in 'FmfM':
    sexo = str (input('Dados Inválido! Digite seu sexo: '))
print(f'Sexo {sexo} registrado!')