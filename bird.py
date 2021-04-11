import pygame
import numpy as np

from constants import *
from copy import deepcopy

from brain import Brain

class Bird():

    def __init__(self, screen):
        self.screen = screen
        self.velocity = 0
        self.gravity = 0.0004
        self.y = HEIGHT*1//3
        self.x = WIDTH*1//3
        self.dead = False

        self.brain = Brain((1, 6))

        self.fitness = 0

        self.rect = pygame.Rect(self.x - 20, self.y - 20, 20, 20)

        self.wdis = 0
        self.hdis = 0

        self.ammount = 0

        self.stupid = False

        self.wall = []

    def draw(self):
        pygame.draw.circle(self.screen, WHITE, (int(self.x), int(self.y)), 20)

    def move(self):
        if self.y < HEIGHT:
            self.y += self.velocity
            self.velocity += 2*self.gravity
        else:
            self.y = HEIGHT

        if self.dead:
            self.x -= 0.2

        self.rect = pygame.Rect(self.x - 20, self.y - 20, 20, 20)
        

    def jump(self):
        if not self.dead and self.velocity >= 0:
            self.velocity = -0.35

    def see(self, walls):

        inputs = []

        for wall in walls:
            if wall.x + wall.thiccness > self.x:
                inputs.append(wall.x - self.x)
                inputs.append(wall.x + wall.thiccness - self.x)
                inputs.append(wall.height - self.y)
                inputs.append(self.y - (wall.height - HOLE))
                inputs.append(self.y)
                inputs.append(HEIGHT - self.y)
                break

        inputs = np.array(inputs)
        inputs /= HEIGHT

        return inputs.T

    def think(self, walls):

        inputs = self.see(walls)
        if not list(inputs):
            return
        outputs = self.brain.feed_forward(inputs)

        
    
        if outputs:
            self.jump()

    def calculate_fitness(self):
        if self.stupid:
            self.fitness = 0
            return 0
        self.fitness = max(0, 100*(2**self.ammount) - self.wdis - self.hdis)
        return self.fitness

    def copy(self):
        baby = Bird(self.screen)
        baby.brain = self.brain.copy()
        return baby

        

        

        
                
                
        
    
    
