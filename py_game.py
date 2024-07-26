# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 02:39:51 2024

@author: atul.sharma
"""

import pygame

from pygame.locals import *

pygame.init()


pygame.display.set_mode((400,500),HWSURFACE|DOUBLEBUF|RESIZABLE)

#pygame.display.set_mode((400,500))

#pygame.display.set_caption('Resizable') 

running =True

while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            running=False
            
    
pygame.quit()