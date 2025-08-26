"""Exercício 014
Curso de Python 3 - Gustavo Guanabara
"""
#Escreva um programa que converta um atemperatura diggitada em °C e converta para °F

c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32

print('A temperatura de {}°C corresponde a {:.2f}°F!'.format(c,f))

