"""Exercício 018
Curso de Python 3 - Gustavo Guanabara
"""
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('=' * 20)
print('SENO: {:.2f}'.format(seno))
print('=' * 20)
print('COSSENO: {:.2f}'.format(cosseno))
print('=' * 20)
print('TANGENTE: {:.2f}'.format(tangente))
print('=' * 20)

