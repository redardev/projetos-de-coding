 #1

letra = input("digite uma letra: ")

vogais = 'aeiou'

if letra in vogais or letra in vogais.upper():
    print("é uma vogal")
else:
    print("é uma consoante")
 #2

preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

if preco1 < preco2:
    if preco1 < preco3:
        print("compre o primeiro produto.")
    else:
        print("compre o terceiro produto.")
else:
    if preco2 < preco3:
        print("compre o segundo produto.")
    else:
        print("compre o segundo terceiro produto.")
#3

número1 = float(input("digite o primeiro número:"))
número2 = float(input("digite o segundo número:"))
número3 = float(input("digite o terceiro número:"))
numeros = [número1, número2, número3]
numeros.sort(reverse=True)
print("numeros em ordem decrescente:",numeros)
#4

turno = input("Em qual turno voçê estuda ? Digite m para matutino, v para vespetino ou n para noturno:")
if turno == "m":
  print("Bom dia!")

elif turno == "v":
    print("Boa tarde!")

elif turno == "n":
   print("Boa noite!")
else:
   print("só pode m,v ou n ")
 #5

dias_da_semana ={
    1:"segunda-feira",
    2:"terça-feira",
    3:"quarta-feira",
    4:"quinta-feira",
    5:"sexta-feira",

}
num = int(input("digite um numero de 1 a 5 ne procure qual o numero da semana se refere:"))

if num in dias_da_semana:
    print(dias_da_semana[num])
else:
    print('numero invalido tente novamente')
#5

nota1 = float(input("digite a primeira nota"))
nota2 = float(input("digite a segunda nota"))
media = (nota1 + nota2) / 2

if 9.0 < media <=10.0:
    conceito = 'a'
elif 7.5 < media <=9.0:
    conceito = 'b'
elif 6.0 < media <= 7.5:
    conceito = 'c'
elif 4.0 < media <= 6.0:
    conceito = 'd'
elif 0< media <= 4.0:
    conceito = 'e'
else:
    conceito = 'conceito inválido'
if  conceito in ['a', 'b', 'c']:
    situacao = 'aprovado'
else:
    situacao = 'reprovado'
print ('media: ', media, 'e seu conceito foi de:' ,conceito,'e voce foi', situacao)
#6
ano = int(input('Digite um ano: '))
if (ano %4 == 0 and ano %100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto..')
else:
    print(f"o ano {ano} não é bissexto..")
 #7

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Qual operação você deseja fazer? (+, -, ., /, ..): ")
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '.':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
elif operacao == '..':
    resultado = num1 ** num2
else:
    print("calculo inválida.")
    resultado = None
if resultado is not None:
    if resultado % 2 == 0:
        tipo1 = "par"
    else:
        tipo1 = "ímpar"

    if resultado >= 0:
        tipo2 = "positivo"
    else:
        tipo2 = "negativo"


    if resultado == int(resultado):
        tipo3 = "inteiro"
    else:
        tipo3 = "decimal"
    print(f"O resultado do calculo é {resultado}, que é um número {tipo1}, {tipo2} e {tipo3}.")

 #8

idade = int(input("digite sua idade:"))
if 0<= idade <= 150:
    print(f'sua idade e de {idade}')
else:
    print('idade inválida tente novamente!')
#9
num = []
for t in range(5):
    numero = float(input(f'digite o {t +1}º numero:'))
    num.append(numero)
    soma = 0
    for numero in num:
        soma += numero
        media = soma / len(num)
        
print(f'a soma dos numeros de: {soma}')
print(f'a media dos numeros deu: {media}')
#10.

sugestao = int(input('coloque um numero inteiro: '))
if sugestao >1:
    for p in range(2, int(sugestao**0.5)+1):
        if sugestao % p ==0:
            print(f'{sugestao} não e primo .')
            
        else:
          print(f'{sugestao} não é um  primo .')
else:
    print(f"{sugestao} não é um  primo.")

#11

temperatura = []

for t in range(5):
    temps = float(input(f'digite a temperatura {t+1}: '))
    temperatura.append(temps)
menor_temperatura = min(temperatura)
maior_temperatura = max(temperatura) 

media_temperaturas = sum(temperatura) / len(temperatura)

print(f'a maior temperatura e: ', {maior_temperatura})
print(f'a menor temperatura e: ',{menor_temperatura})
print(f'a media das temperaturas e de: ',{media_temperaturas})

#12
saldo_medio = float(input("Digite o saldo médio do cliente: "))

if saldo_medio <= 200:
    print(f"Saldo médio: {saldo_medio:.2f}")
    print("Nenhum crédito disponível.")
elif saldo_medio <= 400:
    credito = saldo_medio * 0.2
    print(f"saldo médio: {saldo_medio:.2f}")
    print(f"seu crédito especial é de {credito:.2f}.")
elif saldo_medio <= 600:
    credito = saldo_medio * 0.3
    print(f"saldo médio: {saldo_medio:.2f}")
    print(f"seu crédito especial é de {credito:.2f}.")
else:
    credito = saldo_medio * 0.4
    print(f"saldo médio: {saldo_medio:.2f}")
    print(f"seu crédito especial é de {credito:.2f}.")

#13

nome = input('diga o seu nome: ')
idade = int(input(f'{nome} quantos anos voce tem?? '))

ano = 2024
idade_max = 65
ano_aposentadoria = ano + (idade_max - idade)

print(f'{nome} voce podera se aposentar em {ano_aposentadoria}..')


#14)

valor_hora = float(input("Qual o valor da sua hora de trabalho? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou neste mês? "))


salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 2112.00:
    porcentagem_ir = 0
elif salario_bruto <= 3751.05:
    porcentagem_ir = 0.075
elif salario_bruto <= 4664.68:
    porcentagem_ir = 0.225
else:
    porcentagem_ir = 0.275


desconto_ir = salario_bruto * porcentagem_ir


desconto_sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11


salario_liquido = salario_bruto - desconto_ir - desconto_sindicato


print("\nfolha salarial:")
print(f"salario bruto: R$ {salario_bruto:.2f}\n"
      f"imposto descontado: R$ {desconto_ir:.2f}\n"
      f"desconto do sindicato: R$ {desconto_sindicato:.2f}\n"
      f"FGTS: R$ {fgts:.2f}\n"
      f"salario liquido: R$ {salario_liquido:.2f}")
