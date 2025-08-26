"""Exercício 007
Curso de Python 3 - Gustavo Guanabara
"""

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

m = (n1 + n2) / 2

print('A média entre as notas {} e {} é igual a {}.'.format(n1,n2,m))
