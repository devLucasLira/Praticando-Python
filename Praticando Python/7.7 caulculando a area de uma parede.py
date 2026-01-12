h = int(input('Digite altura da parede: '))
l = int(input('Digite a largura da parede: '))

a = h * l
t = a / 2

print(50*'-')
print('Com base nas informações forneciadas, o resultado da area é: {}M²'.format(a))
print('A tinta usada cobre 2m² por litro, então vai precisar de {}L para pintar tudo'.format(t))
print(50*'-')