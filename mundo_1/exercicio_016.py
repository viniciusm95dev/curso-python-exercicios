"""Exercício 016
Curso de Python 3 - Gustavo Guanabara
"""
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc

n = float(input('Digite um valor qualquer: '))

print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, trunc(n)))

