"""Exercício 006
Curso de Python 3 - Gustavo Guanabara
"""

#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math

n = float(input('Digite um número: '))

d = n * 2
t = n * 3
r = math.sqrt(n)
print('==' * 10)
print('O número digitado foi {}'.format(n))
print('==' * 10)
print('Dobro: {}'.format(d))
print('Triplo: {}'.format(t))
print('Raiz Quadrada: {:.2f}'.format(r))

