"""Exercício 013
Curso de Python 3 - Gustavo Guanabara
"""
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_atual = float(input('Digite seu salário atual:R$'))
aumento = salario_atual * 15 / 100
salario_novo = salario_atual + aumento

print('Seu salário novo com 15% de aumento é R${:.2f}'.format(salario_novo))


