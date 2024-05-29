#patinhos

for patinho in [5, 4, 3, 2, 1]:
    print (patinho, "patinhos foram passear \n Além das montanhas para brincar \n A mamaãe gritou: Quá, quá, quá, quá \n Mas só", patinho-1, " patinhos voltaram de lá")

#mariana
conta = []

for i in range(1, 11):
    conta.append(str(i))
   
    print('Mariana conta', i,'\nMariana conta', i,'Mariana conta', i,'\né',' , é '.join(conta))
    print ('Ana, viva a Mariana, viva a Mariana')
#elefantes

incomodam = 'incomodam, '

for i in range(1, 11):
    if i % 2 == 0:
        if i == 2:
             print(i, 'elefantes ', incomodam * i  , 'muito mais!')
        else:
            print(i, 'elefantes',  incomodam * i ,'muito mais!')
        
    else:
        if i == 1:
            print(i, 'elefante incomoda muita gente')
        else:
            print(i, 'elefantes  incomodam muita gente!')

for i in reversed(range(1, 10)):
    if i % 2 != 0:
        if i == 2:
             print(i, 'elefantes ', incomodam * i  , 'muito mais!')
        else:
            print(i, 'elefantes',  incomodam * i ,'muito menos!')
        
    else:
        if i == 1:
            print(i, 'elefante incomoda muita gente')
        else:
            print(i, 'elefantes  incomodam muita gente!')

    