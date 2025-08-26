"""Exercício 009
Curso de Python 3 - Gustavo Guanabara
"""

# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número para ver sua tabuada: '))

print('Tabuada do Número {}.'.format(num))

for i in range(1, 11):
    print("{} x {:2} = {}".format(num, i, num * i))
