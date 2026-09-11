"""
Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

import math
cateto = float(input("Qual o comprimento do cateto oposto? "))
adja = float(input("Qual o comprimento do cateto adjacente? "))
hipo = math.sqrt(pow(cateto,2) + math.pow(adja,2))
print(f"A hipotenusa sera de {hipo:.2f}")
