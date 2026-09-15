"""
Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

num = int(input("Digite um numero de 0 a 9999: "))
n = str(num)
print(f" Analisando o numero {num} \n Milhar: {n[0]}  \n Centena: {n[1]} \n Dezena: {n[2]} \n Unidade:  {n[3]}")
