"""
Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

import math
angulo = float(input("Informe um angulo: "))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f"O angulo de {angulo} tem o SEN de {seno:.2f}, COS de {cos:.2f} e TAN de {tan:.2f} ")
