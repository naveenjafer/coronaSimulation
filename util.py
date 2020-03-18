def generateMap(dim):
    grid = []
    for i in range(dim):
        temp = []
        for j in range(dim):
            temp.append(0)
        grid.append(temp)
    return grid

def generateMap2(dim):
    grid = [[0 for _ in range(dim)] for _ in range(dim)]
    return grid
