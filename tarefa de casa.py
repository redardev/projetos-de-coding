numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = float(input('Digite um  número real: '))

resultado1 =(2* numero1) * (numero2/2)
print('O produto do dobro do primeiro vezes a metade do segundo é: ',resultado1)

resultado2 = (3 * numero1) + numero2
resultado2cubo = numero3 ** 3
print("A soma do triplo do primeiro com o terceiro é:", resultado2)
print("   O terceiro elevado ao cubo é:", resultado2cubo)



num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


if num1 > num2:
    print("O primeiro número é maior:", num1)
elif num2 > num1:
    print("O segundo número é maior:", num2)
else:
    print("Os números são iguais.")



valor = float(input("Digite um valor: "))

if valor > 0:
    print("O valor é positivo.")
elif valor < 0:
    print("O valor é negativo.")
else:
    print("O valor é zero.")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = (nota1 + nota2) / 2


if media >= 7.0:
    print("Aprovado. Média:", media)
else:
    print("Reprovado. Média:", media)


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior_numero = max(num1, num2, num3)
print("O maior número é:", maior_numero)



