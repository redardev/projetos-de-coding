'''tupla_numeros = (10,20,30)
print(tupla_numeros)
tupla_nova = 10,20,30
print(tupla_nova)
nova_tupla = tuple('teste')
print(nova_tupla)
tupla_nomes = ('marlene', 'Zezinho', 'marlene', 'cibele', 'Zuely')
tupla_nomes.count('Marlene')
print(tupla_nomes.count('suely'))
print(tupla_nomes.count('zezinho'))'''
'''tupla_numeros = (1, 2, 2, 3, 4, 4, 4, 5)
count_4 = tupla_numeros.count(4)
print(count_4)'''

'''dicio = {'chave': 'valor'}
print(type(dicio))'''

d = {'laranjas': 15, 'bananas': 35, 'siriguela': 12}
print(d['bananas'])
#revisando
'''list=[]
tuple=()
dictionary={...:...}'''

d['pitomba'] = 20
print(len(d))
print(d)
print('pitomba' in d)
print('pears' in d)

del d['laranjas']
print('laranjas' in d)

frutas =['pinha', 'oiti coró','jaca','tamarindo']
print([1,2] + [3,4])
print(frutas + [6,7,8,9])
print([0] * 4)
print([1,2, ['oi','tchau']] * 2)