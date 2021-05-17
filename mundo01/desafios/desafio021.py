#tocar um arquivo mp3 pelo python
import pygame
pygame.mixer.init()
pygame.mixer.music.load('mcpoze.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()