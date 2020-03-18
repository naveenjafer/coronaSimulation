import city
import busMap
#import people
if __name__ == "__main__":
    config = {
        "fillFraction" : 0.2,
        "meanPerHouse" : 4,
        "dim" : 100,
        "buildingMultiplier" : 25,
        "busNodes" : 0.1
    }
    c = city.CityMap(config)
    c.placeNodes()
    print(c.verifyNodeFraction())
    print(c.getStatsOnDistributionByBuilding())

    b = busMap.BusMap(config)
    b.placeNodes()
    print(b.verifyNodeFraction())

    
