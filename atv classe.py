#definir tempo e dinheiro
tempo = str(input('O clima está ensolarado? '))
dinheiro = float(input('Quanto de dinheiro Você tem ? '))
#usar os valores das variaveis para definir a situação de ir à praia ou não
if(tempo == 'Sim' and dinheiro > 0): 
    print('Você pode ir á praia') 
    if(tempo == 'Sol' and dinheiro <= 0):
        print('Assista Netflix')     
else:
    print('Assista netflix!') 