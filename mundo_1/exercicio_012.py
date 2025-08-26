"""Exercício 012
Curso de Python 3 - Gustavo Guanabara
"""
#Faça um algoritmo que leia p preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input('Digite o valor do produto:R$'))
preco_desconto = preco_produto * 5 / 100
novo_preco = preco_produto - preco_desconto

print('Valor do produto R${}.'.format(preco_produto))
print('Valor do produto com 5% de desconto:R${:.2f}'.format(novo_preco))

