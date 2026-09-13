"""
Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

import random
um = str(input("Primeiro aluno: "))
dois = str(input("Segundo aluno: "))
tres = str(input("Terceiro aluno: "))
quatro = str(input("Quarto aluno: "))
alunos = [um, dois, tres, quatro]
random.shuffle(alunos)
print(f"O aluno escolhido foi {alunos}")
