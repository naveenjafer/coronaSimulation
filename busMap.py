import numpy as np
import util
from random import seed,random,randint
import copy
from collections import defaultdict
class BusMap():
    def __init__(self, config):
        self.dim = config["dim"]
        self.grid = copy.deepcopy(util.generateMap2(self.dim))
        self.busNodes = config["busNodes"]

    def placeNodes(self):
        count = 0
        target = self.busNodes * (self.dim ** 2)

        while count != target:
            x_rand = randint(0,self.dim-1)
            y_rand = randint(0,self.dim-1)
            if self.grid[x_rand][y_rand] == 0:
                self.grid[x_rand][y_rand] = 1
                count = count + 1

    def verifyNodeFraction(self):
        count = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if self.grid[i][j] != 0:
                    count = count + 1
        return count

    def createRoads(self):
        visited = [[False for _ in range(self.dim)] for _ in range(self.dim)]
        for i in range(self.dim):
            for j in range(self.dim):
                if self.grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    self.bfsRoads(i, j,visited)

    def bfsRoads(self, x, y, visited):
        queue = list()
        queue.append((x, y))

        while len(queue) > 0:
            point = queue.pop()
            x, y = point[0], point[1]
            xWeight = min(x, self.dim - x - 1)
            yWeight = min(y, self.dim - y - 1)
            totalWeight = (xWeight + yWeight)/self.dim
            degree = max(int(float(randint(1, 4)) * totalWeight) + 1,1)
            neighbours = list()
            tmp = list()
            minDist = self.dim**2

            for i in range(x, -1, -1):
                for j in range(y, -1, -1):
                    if self.grid[i][j] == 1 and not visited[i][j]:
                        tmp.append((i, j))
                    if len(tmp) >= degree:
                        minDist = (x-i)**2 + (y-j)**2
                        break
                if len(tmp) >= degree:
                    break
            neighbours.append(list(tmp))
            tmp = list()

            for i in range(x,self.dim):
                for j in range(y,-1,-1):
                    if self.grid[i][j] == 1 and not visited[i][j]:
                        tmp.append((i,j))
                    if len(tmp)>= degree or (x-i)**2 + (y-j)**2 >= minDist:
                        if (x-i)**2 + (y-j)**2 < minDist:
                            minDist = (x - i) ** 2 + (y - j) ** 2
                        break
                if len(tmp) >= degree  or (x-i)**2 + (y-j)**2 >= minDist:
                    break
            neighbours.append(list(tmp))
            tmp = list()

            for i in range(x,-1,-1):
                for j in range(y,self.dim):
                    if self.grid[i][j] == 1 and not visited[i][j]:
                        tmp.append((i,j))
                    if len(tmp) >= degree or (x - i) ** 2 + (y - j) ** 2 >= minDist:
                        if (x - i) ** 2 + (y - j) ** 2 < minDist:
                            minDist = (x - i) ** 2 + (y - j) ** 2
                        break
                if len(tmp) >= degree or (x - i) ** 2 + (y - j) ** 2 >= minDist:
                    break
            neighbours.append(list(tmp))
            tmp = list()

            for i in range(x,self.dim):
                for j in range(y,self.dim):
                    if self.grid[i][j] == 1 and not visited[i][j]:
                        tmp.append((i,j))
                    if len(tmp) >= degree or (x-i)**2 + (y-j)**2 >= minDist:
                        if (x-i)**2 + (y-j)**2 < minDist:
                            minDist = (x - i) ** 2 + (y - j) ** 2
                        break
                if len(tmp) >= degree or (x-i)**2 + (y-j)**2 >= minDist:
                    break
            neighbours.append(list(tmp))

            closest = defaultdict(list)
            for n in neighbours:
                for item in n:
                    key = (x-item[0])**2 + (y-item[1])**2
                    closest[key].append(item)

            closestNeighbours = sorted(closest.items())
            degreeCount = 0
            for dist,pnts in closestNeighbours:
                for pnt in pnts:
                    i,j = pnt[0],pnt[1]
                    if visited[i][j]:
                        continue
                    if degreeCount > degree:
                        break
                    if y<=j:
                        for py in range(y+1,j+1):
                            if self.grid[x][py]==0:
                                self.grid[x][py] = 2
                    else:
                        for py in range(y-1,j-1,-1):
                            if self.grid[x][py] == 0:
                                self.grid[x][py] = 2
                    if x<=i:
                        for px in range(x+1,i+1):
                            if self.grid[px][j] == 0:
                                self.grid[px][j] = 2
                    else:
                        for px in range(x-1,i-1,-1):
                            if self.grid[px][j] == 0:
                                self.grid[px][j] = 2
                    self.grid[i][j] = 1
                    self.grid[x][y] = 1
                    visited[i][j] = True
                    queue.insert(0,(i,j))
                    degreeCount += 1
