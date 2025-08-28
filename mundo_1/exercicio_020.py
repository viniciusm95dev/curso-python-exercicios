"""Exercício 020
Curso de Python 3 - Gustavo Guanabara
"""
#Sortear a ordem de apresentação de trabalho.
from random import shuffle

n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')

lista = [n1, n2, n3, n4]

shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)