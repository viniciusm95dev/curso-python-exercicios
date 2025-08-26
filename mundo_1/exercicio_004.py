"""Exercício 004
Curso de Python 3 - Gustavo Guanabara
"""

#Faça um programa que leia aldo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

s = input('Digite algo: ')

print(type(s))
print(s.isalnum())
print(s.isalpha())
print(s.isascii())
print(s.isdecimal())
print(s.isidentifier())
print(s.isnumeric())

