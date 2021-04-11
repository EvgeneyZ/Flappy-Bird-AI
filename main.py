import sys
import pygame
import time

from constants import *

from bird import Bird
from wall import Wall

from population import Population

bird_killer = False
GEN = 1


def run_game():

    global bird_killer
    global GEN

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Flappy Bird AI")

    pop = Population(screen, 50)

    walls = []
    timer = 0

    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_killer = True
                elif event.key == pygame.K_UP:
                    pop = Population(screen, 50)
                    print("==========================================")
                    print("Reboot")
                    print("==========================================")
                    GEN = 1

        draw(screen, pop, walls)

        if not pop:
            print("GENERATION", GEN)
            print("Highscore:", sorted(pop.group, key = lambda k : k.ammount, reverse = True)[0].ammount)
            print("------------------------------------------")
            GEN += 1
            walls = []
            timer = 0
            pop.selection()
            pop.mutate()

        timer -= 1
        if timer <= 0:
            timer = 2000
            if walls:
                new_wall = walls[-1].copy()
                new_wall.thiccness += 1
                walls.append(new_wall)
            else:
                walls.append(Wall(screen))


def draw(*pack):
    global bird_killer
    
    screen = pack[0]
    pop = pack[1]
    walls = pack[2]

    screen.fill(bg_color)

    for wall in walls:
        
        if wall:
            wall.move()
            wall.draw()
            for bird in pop.group:
                if bird.dead:
                    continue
                if wall.rect1.colliderect(bird.rect) or wall.rect2.colliderect(bird.rect) or bird.y <= 0 or bird.y >= HEIGHT or bird_killer:
                    bird.dead = True
                    bird.wdis = wall.x + wall.thiccness/2 - bird.x
                    bird.hdis = abs((wall.height - HOLE/2) - bird.y)
                    if bird.y <= 0 or bird.y >= HEIGHT:
                        bird.stupid = True
                elif bird.x > wall.x + wall.thiccness*3/8 and bird.x < wall.x + wall.thiccness*5/8 and bird.y > wall.height - HOLE and bird.y < wall.height:
                    if wall not in bird.wall:
                        bird.ammount += 1
                        bird.wall.append(wall)
        else:
            walls.remove(wall)

    if bird_killer:
        bird_killer = False
    
    pop.update(walls)
    pygame.display.flip()

run_game()
