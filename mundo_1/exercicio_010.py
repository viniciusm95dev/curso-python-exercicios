"""Exercício 010
Curso de Python 3 - Gustavo Guanabara
"""

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.


import requests

def obter_cotacao_dolar():
    url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    resposta = requests.get(url)
    dados = resposta.json()
    return float(dados['USDBRL']['bid'])

def converter_real_para_dolar(valor_real):
    cotacao = obter_cotacao_dolar()
    valor_dolar = valor_real / cotacao
    return valor_dolar

if __name__ == '__main__':
    try:
        valor_real = float(input("Digite o valor em Reais (R$): "))
        valor_dolar = converter_real_para_dolar(valor_real)
        print(f"R$ {valor_real:.2f} equivalem a US$ {valor_dolar:.2f}")
    except ValueError:
        print("Por favor, insira um valor numérico válido.")
