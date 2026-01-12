n1 = int(input ('Digite um numero: '))
n2 = int(input ('Digite um numero: '))

s = n1 + n2 
m = n1 * n2
d = n1 / n2 
di = n1 // n2 
e = n1 ** n2 

print (' A soma é: {} \n A multiplicação é: {} \n A divisão é: {}' .format (s,m,d), end=' ') #\n quebra a linha, e, end=' poder por algo dentro das aspas tambem' pra juntar o print de cima com o de baixo
print (' A Divisao inteira é: {} \n A exponenciação é:{}' .format (di,e)) # . format pra evitar ficar digitando de mais 
print (40*'/') 
print ('Obrigado por usar meu sistema !!')
print (40*'/') # Atalho para printar repetição 