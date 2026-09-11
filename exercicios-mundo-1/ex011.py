"""
Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

altura = float(input("Informe o valor da altura da parede: "))
largura = float(input("Informe o valor da largura da parede: "))
area = altura * largura
print(f"A area é {area}, a quantidade de tinta necessaria para pintar é {area/2} litros")
