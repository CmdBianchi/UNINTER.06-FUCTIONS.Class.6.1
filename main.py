########################################################################
#-------------> Exercicio 01 | TUPAS

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)

('Machado', 'Camisa', 'Bacon', 'Abacate')

print(mochila[0]) #print do elemento 1 - Indice 0
print(mochila[2]) #Print do elemento 3 - Indice 2
print(mochila[0:2]) #Print dos Elementos 1 e 2 - Indice 0 e 1
print(mochila[2:]) #Print dos elementos a partir do indice 2
print(mochila[-1]) #Print do ultimo

for item in mochila:
    print('Na minha mochila tem: {}'.format(item))
print('\n')
#-----------------------------> Forma menos simplificada

#tam = len(mochila)
#for i in range(0, tam, 1):
    #print('Na minha mochila tem: {}'.format(mochila[i]))
#print('\n')

#--------------------------------------------------------#

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade

print(mochila)
print(upgrade)
print(mochila_grande)

mochila_grande_invertida = upgrade + mochila
print(mochila_grande)
print(mochila_grande_invertida)

########################################################################
#-------------> Exercicio 02 | TUPAS

def soma(*num):
    soma = 0
    print('Tupla: {}'.format(num))
    for i in num:
        soma += i
    return soma

print('Resultado : {}\n'.format(soma(1,2)))
print('Resultado : {}\n'.format(soma(1, 2, 3, 4, 5, 6, 7, 8, 9,)))

########################################################################
#-------------> Exercicio 03 | LISTA

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista: ', mochila)

mochila[2] = 'Laranja'
print('Lista: ', mochila)

########################################################################
#-------------> Exercicio 04 | LISTA

mochila.append('Ovos')
print('Lista: ', mochila)

mochila.insert(1, 'Canivete')
print('Lista: ', mochila)

del mochila[1]
print('Lista: ', mochila)
mochila.remove('Ovos')
print('Lista: ', mochila)

########################################################################
#-------------> Exercicio 05 | LISTA

x = [5, 7, 9, 11]
y = x
print(x)
print(y)

y[0] = 2
print(x)
print(y)

x = [5, 7, 9, 11]
y = x[:]
print(x)

########################################################################
#-------------> Exercicio 05 | STRINGS DENTRO DE LISTAS

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0])

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0][0])
print(mochila[2][1])

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for item in mochila:
    for letra in item:
        print(letra, end='')
print()

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for i in range(0, len(mochila), 1):
    for j in range(0, len(mochila[i]), 1):
        print(mochila[i][j], end ='')
    print()

########################################################################
#-------------> Exercicio 06 | STRINGS DENTRO DE LISTAS

item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item: '))
    item.append(int(input('Digite o valor: ')))
    item.append(float(input('Digite o valor: ')))
    mercado.append(item[:])
    item.clear()
print(mercado)

########################################################################
#-------------> Exercicio 07 | DICIONARIOS

game = {'nome': 'Super Mario',
        'Desenvolvedor':'Nintendo',
        'Ano':1990}
print(game)

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

print(game.values())

for i in game.keys():
    print(i)

print(game.keys())

for i in game.keys():
    print(i)

print(game.items())
for i,j in game.items():
    print('{} = {}'.format(i, j))

