"""Exercício 017
Curso de Python 3 - Gustavo Guanabara
"""
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('COmprimento do cateto adjacente: '))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))