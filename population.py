from bird import Bird
import random

from copy import deepcopy

class Population():

    def __init__(self, screen, numb):

        self.screen = screen
        self.size = numb
        self.group = []

        for i in range(self.size):
            self.group.append(Bird(self.screen))



    def update(self, walls):

        for bird in self.group:
            if not bird.dead:
                bird.think(walls)
                bird.move()
                bird.draw()

    def __bool__(self):
        for bird in self.group:
            if not bird.dead:
                return True
        return False

    def calculate_fitnesses(self):
        self.sum_fitness = 0.001
        for bird in self.group:
            self.sum_fitness += bird.calculate_fitness()

    def choose_best(self):
        fit = self.group[0].fitness
        best = self.group[0]

        for bird in self.group:
            if bird.fitness > fit:
                fit = bird.fitness 
                best = bird
                
        return best.copy()

    def selection(self):
        self.calculate_fitnesses()
        new_group = []
        best = self.choose_best()
        new_group.append(best)

        pool = []
        for bird in self.group:
            numb = max(1, int(self.size * (bird.fitness/self.sum_fitness)))
            for _ in range(numb):
                pool.append(bird)


        for i in range(1, self.size):
            parent1 = random.choice(pool)
            parent2 = random.choice(pool)
            baby = Bird(self.screen)
            w, b =parent1.brain.crossover(parent2.brain)
            baby.brain.w = deepcopy(w)
            baby.brain.b = deepcopy(b)
            new_group.append(baby)

        self.group = new_group

    def choose_parent(self, parent = None):
        running_sum = 0
    
        for bird in self.group:
            if bird == parent:
                continue
            running_sum += bird.fitness
            if running_sum * random.random() > self.sum_fitness:
                return bird.copy()

        return self.group[0].copy()

    def mutate(self):

        for i in range(1, self.size):
            self.group[i].brain.mutate()
            

    
