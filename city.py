import numpy as np
from matplotlib import pyplot as plt
import config
import random

# Initialize city grid with given size. Values start with zero to indicate the prescence of no home.
def initCity():
    for i in range(cartToIndex(config.x,config.y)):
        config.cityGrid.append(
            {
                'date': config.date,
                'desperation': random.random(),
                'bid': 0,
                'ask': 0,
                'x': 0,
                'y': 0,
                'beds': 0,
                'baths': 0,
                'sqft': 0,
                'distance': 0
            }
        )

def cartToIndex(x,y):
    return (y - 1) * config.x + (x - 1)

# Populates coordinates of each home giving them a location in the City Grid. Location can be used to find distance from
# the center and will be used at some point to allow homes to propegate outward. This func generates a circle.
def genCircHomes(r):
    for i in range(config.x):
        for n in range(config.y):
            if (i-(config.x/2))**2 + (n-(config.y/2))**2 < r**2:
                # Set coordinates of each home
                config.cityGrid[cartToIndex(i,n)]['x'] = i
                config.cityGrid[cartToIndex(i,n)]['y'] = n

# Populates coordinates of each home giving them a location in the City Grid. Location can be used to find distance from
# the center and will be used at some point to allow homes to propegate outward. This func generates a rectangle.
def genRectHomes(xDim=config.x,yDim=config.y):
    for i in range(config.x):
        for n in range(config.y):
            if (config.y/2 - yDim/2) <= n < (config.y/2 + yDim/2) and (config.x/2 - xDim/2) <= i < (config.x/2 + xDim/2):
                # Set coordinates of each home
                config.cityGrid[cartToIndex(i, n)]['x'] = i
                config.cityGrid[cartToIndex(i, n)]['y'] = n

# Depricated get dimension function
# def getDimensions(cityGrid):
#     x = len(cityGrid)
#     y = len(cityGrid[0])
#     return x,y

# Plots the city grid space and associated full/empty homes. Mostly used for debug.
def plotHomes():
    plotGrid = np.zeros((config.x,config.y))
    for i in range(config.x):
        for n in range(config.y):
            if config.cityGrid[cartToIndex(i,n)]['x'] != 0 and config.cityGrid[cartToIndex(i,n)]['y'] != 0 :
                plotGrid[i, n] = 1
    plt.imshow(plotGrid, interpolation='none')
    plt.show()

# Counts the number of homes currently on the city grid.
def countHomes():
    count = 0
    for i in range(config.x):
        for n in range(config.y):
            if config.cityGrid[cartToIndex(i,n)]['x'] != 0 and config.cityGrid[cartToIndex(i,n)]['y'] != 0 :
                count += 1
    return count

initCity()
genCircHomes(30)
print(countHomes())
print(config.cityGrid)
plotHomes()
