"""
Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
"""

real = float(input("Quantos reais voce tem? "))
print(f"Voce tem R$ {real:.2f} e pode comprar {real / 5.26:.2f} dolares, pode comprar {real / 6.07:.2f} euros, pode comprar {real/0.75:.2f} wuan")
