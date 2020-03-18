import numpy as np
import util
from random import seed,random,randint
import copy

class BusMap():
    def __init__(self, config):
        self.dim = config["dim"]
        self.map = copy.deepcopy(util.generateMap2(self.dim))
        self.busNodes = config["busNodes"]

    def placeNodes(self):
        count = 0
        target = self.busNodes * (self.dim ** 2)

        while count != target:
            x_rand = randint(0,self.dim-1)
            y_rand = randint(0,self.dim-1)
            if self.map[x_rand][y_rand] == 0:
                self.map[x_rand][y_rand] = 1
                count = count + 1

    def verifyNodeFraction(self):
        count = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if self.map[i][j] != 0:
                    count = count + 1
        return count
