l =[]

print(dias[0])
print(dias[1])#print(dias[2])

z =[3,8,9]
z[0] = 7
print(z)

v = [6,7,5,8,9]
z = v
print(z)

a =[81,82,83]
b = a[:] #cria um clone com fatia
print(a == b)
print(a is b)
b[0] = 5
print(a)
print(b)


uma_lista = ['a', 'b', 'c','d','e','f']
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[:])                                               

minhaLista=[76,92.3,'oi',True,4,76]
minhaLista1=['pitomba',76]
minhaLista2= minhaLista + minhaLista1
minhaLista2[3]='Cibele'
minhaLista[0]=99
Listafinal= minhaLista + minhaLista2
print(Listafinal)
print(Listafinal[2])

uma_lista =[4,2,8,6,5]
uma_lista = uma_lista + ['Cibele']
print(uma_lista)