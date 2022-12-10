import market, statcurves, city, orderbook, config

# type of curve to use for bathroom distribution, can be "normal" or "skew"
bathroomDist = "normal"
# parameters for normal distribution of bedrooms. in order is: detail, min, max, amount to generate, standard dev
bathroomNormalParams = [1,1,6,config.x*config.y,0.25]
# parameters for skew distribution of bedrooms. in order is: detail, min, max, amount to generate, standard dev, scale, skewness, location
bathroomSkewParams = [1,1,6,config.x*config.y,0.25,1,3,0]

# type of curve to use for bedroom distribution, can be "normal" or "skew"
bedroomDist = "normal"
# parameters for normal distribution of bedrooms. in order is: detail, min, max, amount to generate, standard dev
bedroomNormalParams = [1,1,6,config.x*config.y,0.25]
# parameters for skew distribution of bedrooms. in order is: detail, min, max, amount to generate, standard dev, scale, skewness, location
bedroomSkewParams = [1,1,6,config.x*config.y,0.25,1,3,0]

if __name__ == '__main__':
    print("hi")