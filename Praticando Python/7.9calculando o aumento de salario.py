n = input('Por favor, Digite seu nome: ')
print(50*'-')
print('Olá {} é um prazer te ver por aqui !!'.format(n))
print('')
s = int(input('Agora vamos ao que interessa, vamos calcular seu aumento. digite seu salario atual: '.format(n)))
print(50*'-')
au = s * 15 / 100

ns = s + au 

print('Parabens {} voce teve um aumento de 15%, e seu salario passa de R${} para R${}'.format(n,s,ns))
print('')
print('Espero que continue evoluindo, ate Breve !!')
print(50*'-')