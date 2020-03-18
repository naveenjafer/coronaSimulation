def generateMap(dim):
    map = []
    for i in range(dim):
        temp = []
        for j in range(dim):
            temp.append(0)
        map.append(temp)
    return map

def generateMap2(dim):
    map = [[0 for _ in range(dim)] for _ in range(dim)]
    return map
