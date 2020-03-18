from random import seed,random,randint
import numpy as np
import util
import copy

seed(1)
np.random.seed(0)
class CityMap():
    def __init__(self, config):
        '''
        Total number of building nodes = 0.2 * w * h
        Building types?
            bus_node - 1 - 5
            work_node - 2 - 20
            house_node - 3 - 50
            restaurant_node - 4 - 5
            school_node - 5 - 5
            market_node - 6 - 5
            hospital_node - 7 - 5
            misc_node - 8 - 5
        '''
        self.map = []
        self.dim = config["dim"]
        self.fillFraction = config["fillFraction"]
        self.config = {
            "work_node" : {
                "id" : 1,
                "share" : 0.1,
                "avg_den" : 20
            },
            "house_node" : {
                "id" : 2,
                "share" : 0.5,
                "avg_den" : 25
            },
            "stores_node" : {
                "id" : 3,
                "share" : 0.1,
                "avg_den" : 15
            },
            "misc_node" : {
                "id" : 4,
                "share" : 0.1,
                "avg_den" : 20
            },
            "school_node" : {
                "id" : 5,
                "share" : 0.1,
                "avg_den" : 5
            },
            "resto_node" : {
                "id" : 6,
                "share" : 0.1,
                "avg_den" : 10
            }
        }
        self.map = copy.deepcopy(util.generateMap(self.dim))

    def placeNodes(self):
        for key in self.config:
            print("Placing items ", key)
            count = 0
            mean = self.config[key]["avg_den"]
            std = 0.2*self.config[key]["avg_den"]
            size = int(self.dim * self.dim * self.fillFraction * self.config[key]["share"])

            print("Mean: ", mean, " Std: ", std, " Size: ", size)
            distArray = np.random.normal(mean, std, size)
            distArray = list(distArray)
            target = self.config[key]["share"] * self.dim * self.dim * self.fillFraction

            while count != target:
                x_rand = randint(0,self.dim-1)
                y_rand = randint(0,self.dim-1)
                if self.map[x_rand][y_rand] == 0:
                    self.map[x_rand][y_rand] = {"id" : self.config[key]["id"], "count" : int(distArray[count]) }
                    count = count + 1

    def verifyNodeFraction(self):
        count = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if self.map[i][j] != 0:
                    count = count + 1
        return count

    def getStatsOnDistributionByBuilding(self):
        stats_obj = {}
        for i in range(self.dim):
            for j in range(self.dim):
                if self.map[i][j] != 0:
                    if self.map[i][j]["id"] in stats_obj.keys():
                        stats_obj[self.map[i][j]["id"]] = stats_obj[self.map[i][j]["id"]] + self.map[i][j]["count"]
                    else:
                        stats_obj[self.map[i][j]["id"]] = self.map[i][j]["count"]
        return stats_obj
