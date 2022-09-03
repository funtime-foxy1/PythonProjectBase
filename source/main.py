# Pygame boiler plate
# Should have a red square on screen if run
# pip3 install pygame

from queue import Empty
from tokenize import String
import pygame
from pygame.locals import *

class Colors:
  RED = (255, 0, 0)
  BLUE = (0, 0, 255)
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)


class Guy:
  guyX = 20
  guyY = 20
  speed = 0.2
  guyLEFT = pygame.image.load("textures/debug/demoPerson_white_left.png")
  guyRIGHT = pygame.image.load("textures/debug/demoPerson_white_right.png")
  guyBLACK = pygame.image.load("textures/debug/demoPerson_black.png")
  direction = 'R'
  
  def update(screen):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] or keys[pygame.K_UP]:
      Guy.guyY-=Guy.speed
      
    if keys[pygame.K_s]or keys[pygame.K_DOWN]:
      Guy.guyY+=Guy.speed
      
    if keys[pygame.K_d]or keys[pygame.K_RIGHT]:
      Guy.guyX+=Guy.speed
      Guy.direction = 'R'
      
    if keys[pygame.K_a]or keys[pygame.K_LEFT]:
      Guy.guyX-=Guy.speed
      Guy.direction = 'L'
      
    if Guy.direction == 'R':
      screen.blit(Guy.guyRIGHT, (Guy.guyX,Guy.guyY))
    if Guy.direction == 'L':
      screen.blit(Guy.guyLEFT, (Guy.guyX,Guy.guyY))


#Setup pygame window

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Guy Test Thingy")
pygame.display.set_icon(Guy.guyBLACK)


running = True
while running:
  screen.fill(Colors.BLACK)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  Guy.update(screen)
  
  pygame.display.flip()

    
pygame.quit()