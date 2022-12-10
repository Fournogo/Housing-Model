import numpy as np
import pandas as pd
import random
import config

def addorder(desperation, bid, ask, x, y):
    config.orderbook.append({'desperation': desperation,'bid': bid,'ask': ask,'x': x,'y':y})

def generateorder(index):
    runningsum = 0
    runningtotal = 0
    for i in range(len(config.orderbook)):
        if config.orderbook[i]['beds'] == config.cityGrid[index]['beds']:
            runningsum += config.orderbook[i]['bid']
            runningtotal += 1
    avgBid = runningsum/runningtotal

    desperation = random.random()
    config.orderbook.append(
        {
            'date': date,
            'desperation': desperation,
            'bid': bid,
            'ask': ask,
            'x': x,
            'y':y,
            'beds': beds,
            'baths': baths,
            'sqft': sqft,
            'distance': dist
         }
    )

addorder(0.1, 100000, 90000, 100, 100)
addorder(0.9, 300000, 190000, 200, 200)
print(config.orderbook)
print(generateorder())
