"""
Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""

import random
um = str(input("Primeiro aluno: "))
dois = str(input("Segundo aluno: "))
tres = str(input("Terceiro aluno: "))
quatro = str(input("Quarto aluno: "))
alunos = [um, dois, tres, quatro]
escolha = random.choice(alunos)
print(f"O aluno escolhido foi {escolha}")
