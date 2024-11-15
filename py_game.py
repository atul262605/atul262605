# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 02:39:51 2024

@author: atul.sharma
"""

import pygame
# Form screen with 400x400 size 
# and with resizable 
pygame.init()
screen = pygame.display.set_mode((400, 400),  
                                 pygame.RESIZABLE) 
  
# set title 
pygame.display.set_caption('Resizable') 

color=(22,205,555)

screen.fill(color)
pygame.display.flip()
  
# run window 
running = True
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
  
# quit pygame after closing window 
pygame.quit()