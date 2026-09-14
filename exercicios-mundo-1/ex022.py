"""
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
"""

nome = str(input("Digite o seu nome: ")).strip()
separa = nome.split()
print("Analisando o seu nome:")
print(f"Com todas as letras maiusculas: {nome.upper()}")
print(f"Com todas as letras minusculas: {nome.lower()}")
print(f"Quantas letras ao todo {len(nome) - nome.count(' ')} ")
print(f"O primeiro nome tem {nome.find(' ')} letras")
print(f"O seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras ")
