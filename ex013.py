"""
Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input("Informe o seu salario: "))
salarionovo = salario + (salario * 0.15)
print(f"Seu salario é {salario:.2f} e seu novo salario com aumento é {salarionovo:.2f}")
