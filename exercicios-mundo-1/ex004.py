"""
Desafio 004
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""
palavra = input('Escreve uma palavra: ')
print('O tipo primitivo dessa palavra é', type(palavra))
print('Só tem espaços?', palavra.isspace())
print('É um numero?', palavra.isnumeric())
print('É alfabetico', palavra.isalpha())
print('É alfanumerico?', palavra.isalnum())
print('Está em letras MAIUSCULAS?', palavra.isupper())
print('Esta em letras minusculas', palavra.islower())
print('Esta capitalizada', palavra.istitle())
