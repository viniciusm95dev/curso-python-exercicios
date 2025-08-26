"""Exercício 005
Curso de Python 3 - Gustavo Guanabara
"""

#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

n = int(input('Digite um número inteiro: '))

a = n - 1
s = n + 1

print('O número {} tem com seu sucessor {} e antecessor {}.'.format(n, s, a))
