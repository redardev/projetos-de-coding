'''for produto in range(0, 4):
    p = str(input('digite o nome do produto: '))
    v = float(input('digite o valor do produto: '))'''

'''for elemento in [1,2,3,4,5,6]:
    print('Estamos no elemento ', elemento)'''
'''for elemento in 'STRING':
    print('estamos no elemento ', elemento)'''
'''for elemento in range(len('STRING')):
    print('estamos no elemento ',elemento)'''

'''produto = 0
while produto < 4:
    p = str(input('digite o nome do produto '))
    v = float(input('digite o valor do produto'))
    produto += 1'''

'''elemento = 0
while elemento <= len([1,2,3,4,5,6]):
    print('Estamos no elemento ', elemento)
    elemento += 1
'''

'''
s= 'STRING'
indice = 0

while indice in range (len(s)):
    print('Estamos no elemento ', s[indice])
    indice +=1'''
'''
palavra = 'tranquilo'
for indice, letra in enumerate(palavra):
    print(indice, letra)'''

'''s = 'viva o python'
for ch in s[3:8]:
    print('oi') 
'''

pares = 0
impares = 0
for i in range(10):
    numero = int(input("Digite um número inteiro: ")) 
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)