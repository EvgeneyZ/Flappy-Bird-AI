import numpy as np
import random

class Brain():

    def __init__(self, shape):
        self.shape = shape

        self.w = 2*np.random.random(size = shape) - 1
        self.b = 2*np.random.random(size = (1)) - 1


    def feed_forward(self, X):

        outputs = self.w@X + self.b
        return self.activate(outputs)

    def activate(self, a):
        return a>0

    def mutate(self):
        for i in range(len(self.w)):
            for j in range(len(self.w[0])):
                a = random.random()
                if a < 0.3:
                  self.w[i][j] += random.choice([0.01, -0.01, 0.05, -0.05])
                if a < 0.01:
                    self.w[i][j] = random.random()*2 - 1
        a = random.random()
        if a < 0.3:
            self.b += random.choice([0.01, -0.01, 0.05, -0.05])
        if a < 0.01:
            self.b = random.random()*2 - 1

    def crossover(self, partner):
        baby = Brain(self.shape)
        
        for i in range(len(self.w)):
            for j in range(len(self.w[0])):
                baby.w[i][j] = (self.w[i][j] + partner.w[i][j])/2

            
        baby.b = (self.b + partner.b)/2
        return baby.w, baby.b

    def copy(self):
        copy = Brain(self.shape)
        copy.w = self.w
        copy.b = self.b
        return copy

