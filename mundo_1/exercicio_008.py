"""Exercício 008
Curso de Python 3 - Gustavo Guanabara
"""

#Escreva um programa que leia um valor em metros e o exiba converido em centímetros e milímetros.

m = float(input('Medida em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('=' * 35)
print('A medida de {}m corresponde a: '.format(m))
print('=' * 35)
print('Quilômetros: {}km.'.format(km))
print('Hectômetros: {}hm.'.format(hm))
print('Decâmetros: {}dam.'.format(dam))
print('Decímetros: {}dm.'.format(dm))
print('Centímetros: {}cm'.format(cm))
print('Milímetros: {}mm.'.format(mm))
print('=' * 35)
