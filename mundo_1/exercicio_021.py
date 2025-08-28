"""Exercício 021
Curso de Python 3 - Gustavo Guanabara
"""
#Arquivo MP3

import pygame

# Inicializar pygame
pygame.mixer.init()

# Carregar música
pygame.mixer.music.load('ex021.py.MP3')

print("Comandos:")
print("1 - Play")
print("2 - Stop")
print("0 - Sair")

while True:
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        pygame.mixer.music.play()
        print("🎵 Música tocando...")
    
    elif opcao == '2':
        pygame.mixer.music.stop()
        print("⏹️ Música parada")
    
    elif opcao == '0':
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        print("👋 Saindo...")
        break
    
    else:
        print("❌ Opção inválida!")