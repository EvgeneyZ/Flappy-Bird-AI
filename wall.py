import pygame
import random

from constants import *



class Wall():

    def __init__(self, screen):
        self.screen = screen
        self.thiccness = 50
        self.height = HEIGHT // 2 + random.randint(-150, 150)
        self.x = WIDTH - 100
        self.rect1 = pygame.Rect(self.x, self.height,
                     self.thiccness, HEIGHT)
        
        self.rect2 = pygame.Rect(self.x, 0,
                     self.thiccness, self.height - HOLE)

        self.velocity = -.2


    def draw(self):
        pygame.draw.rect(self.screen, GREEN, self.rect1)
        pygame.draw.rect(self.screen, GREEN, self.rect2)

    def move(self):
        self.x += self.velocity
        self.rect1 = pygame.Rect(self.x, self.height,
                     self.thiccness, HEIGHT)
        
        self.rect2 = pygame.Rect(self.x, 0,
                     self.thiccness, self.height - HOLE)

        

    def __bool__(self):
        return self.x + self.thiccness > 0

    def copy(self):
        wall = Wall(self.screen)
        wall.thiccness = self.thiccness
        return wall
