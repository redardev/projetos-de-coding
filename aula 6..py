#ver o ano e preço do carro
anoCarro = int(input("Qual o ano do seu carro? "))
precoCarro = float(input('Qual o preço do seu carro:'))
#calculo da taxa
if(anoCarro < 1990):
    print("Você pagará uma taxa de: ", precoCarro * 0.01 )
else:
    print('Você pagará uma taxa de: ', precoCarro * 0.015)

#Fazer a separação dos cargos
cargo = int(input("Digite o codigo do seu cargo: "))
salario = float(input('Digite seu salário: '))
#calculo do salario
if(cargo == 101):
    print('Seu aumento de salário será de 10% e seu novo salário será de: ', salario + (salario * 0.1), 'seu aumento de salario será de: ', (salario * 0.1))
elif(cargo == 102):
     print('Seu aumento de salário será de 20% e seu novo salário será de: ', salario + (salario * 0.2), 'seu aumento de salario será de: ', (salario * 0.2))
elif (cargo == 103):
     print('Seu aumento de salário será de 30% e seu novo salário será de: ', salario + (salario * 0.3), 'seu aumento de salario será de: ', (salario * 0.3))
else:
     print('Seu aumento de salário será de 40% e seu novo salário será de: ', salario + (salario * 0.4), 'seu aumento de salario será de: ', (salario * 0.4))


