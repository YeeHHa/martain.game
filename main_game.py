import os
import pygame
import sys

WIDTH, HEIGHT = 360, 480
FPS = 60
pygame.init() 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("martian game") 

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()


    screen.fill((0,0,0))
    pygame.display.flip()



