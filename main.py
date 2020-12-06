import pygame
import os
import pong
import time
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
running = True
onscreenmenuitems = []
onscreenentities = []
background = None
pygame.display.toggle_fullscreen()


'''
game start
'''
if __name__ == "__main__":
    while True:
        game = pong.game(screen)
        game.play()

pygame.quit()
