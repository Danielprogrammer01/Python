idade = int(input('Digite sua idade: '))
print('')

if idade >= 0 and idade <= 12:
    print(f'Sua idade é {idade} anos. Você é uma CRIANÇA')
    print('')
elif idade >= 13 and idade <= 17:
    print(f'Sua idade é {idade} anos. Você é um ADOLESCENTE')
    print('')
elif idade >= 18 and idade <= 59:
    print(f'Sua idade é {idade} anos. Você é um ADULTO')
    print('')
else:
    print(f'Sua idade é {idade} anos. Você é um IDOSO')
    print('')
    