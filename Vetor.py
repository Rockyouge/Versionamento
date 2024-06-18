#Faça um programa que peça a idade e altura de 5 pessoas, armazene cada informação
#no seu respectivo vetor. Imprima a idade e a altura na ordem inversa da listada.

Idades = []
Alturas = []

contador = 0

while contador < 5:
    Idade = int(input(f"Digite a sua idade {contador + 1}:"))
    Altura = float(input(f"Digite a sua altura {contador + 1}:"))
    Idades.append(Idade)
    Alturas.append(Altura)
    contador += 1

print(Idades[::-1])

print(Alturas[::-1])
