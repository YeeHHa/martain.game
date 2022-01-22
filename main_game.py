#!/usr/bin/python3
import os
import pygame
import sys
import random 
import time

WIDTH, HEIGHT = 1700, 700
FPS = 60
pygame.init() 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("martian game") 
number = 5
clock = pygame.time.Clock()
a = 10 
phi = 1.618

b = a // phi
x , y = WIDTH//2, HEIGHT//2
dots = [ pygame.Surface((a, b)) for x in range(random.randrange(1,7000)) ]

for dot in dots:
    
    dot.fill((random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)))

test_player = pygame.Surface((10,10))

test_player.fill((25,89,100))
test_sur = pygame.Surface((10,10))
screen.fill((0,0,0))

def raw():
    x = random.randrange(-6, 10)
    if x < 0:
        return -1
    else:
        return 1

    if x == -6 or x == 10:
        return x


def drawl():
    screen.fill((0,0,0))
    x , y = 360//2, 480//2 
    print(f'x : {x} y : {y}')
    for dot in dots:
        x  += phi*y
        y += x//phi

        screen.blit(dot, (x, y))
        print(f'number = {number}')
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                number -= 1
            if event.key == pygame.K_DOWN:
                number += 1
    
    screen.fill((0,0,0))
#    x, y = WIDTH//2 , HEIGHT//2
    for dot in dots:
        if x < 0 or x > WIDTH:
            x = random.randrange(0, WIDTH)
        if y < 0 or y > HEIGHT:
            y = random.randrange(0, HEIGHT)

        baw = raw()

        x +=baw * (phi * y)
        y += baw *(x//phi)


        screen.blit(dot, (x, y))

    time.sleep(0.1)
    pygame.display.flip()



