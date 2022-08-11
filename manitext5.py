nome = str(input('Digite seu nome completo: ')).strip()

x = nome.find(' ')
y = nome.rfind(' ')+1

print('Muito prazer em te conhecer!')

print('Seu primeiro nome é {}'.format(nome[:x]))
print('Seu último nome é {}'.format(nome[y:]))

#ou

n = str(input('Digite seu nome completo: ')).strip()

nome = n.split()

print('Muito prazer em te conhecer!')

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))



