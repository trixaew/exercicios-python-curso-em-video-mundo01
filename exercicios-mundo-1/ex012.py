"""
Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

preço = float(input("Informe o preço do produto: "))
desconto = preço - (preço * 0.05)
print(f"O valor do produto é {preço} o valor do desconto é R$ {preço * 0.05:.2f} e o novo valor é {desconto:.2f} ")
