"""Exercício 015
Curso de Python 3 - Gustavo Guanabara
"""
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

km = float(input('Quantidade de Km percorridos: '))
dia = int(input('Quantidade de Dias alugado: '))

total_pagar = (km * 0.15) + (dia * 60)

print('Total a pagar:R${:.2f}'.format(total_pagar))

