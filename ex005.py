"""
Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

numero = int(input("Digite um numero: "))
ant = numero - 1
sucess = numero + 1
print(f"O numero é: {numero}")
print(f"O antecessor desse numero é {ant} e o sucessor é {sucess}")
