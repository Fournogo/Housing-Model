import math
from scipy.integrate import quad
import random

# Generates a normal distribution with respect to x. Integral of the curve formed should equal 1.00
def normalDist(x,mean,std):
    return float(math.exp(-0.5 * ((x-mean) / std) ** 2) / (std * math.sqrt(2*math.pi)))

# Generates a skewed distribution with respect to x. Integral of the curve formed should equal 1.00
def skewedDist(x,loc=0,scale=1,skew=5,mean=0,std=1):
    Px = (skew * ((x - loc) / scale))
    P = 0.5 * (1 + math.erf(Px / math.sqrt(2)))
    Fx = (x - loc) / scale
    F = normalDist(Fx,mean,std)
    return float((2 / scale) * F * P)

# Generates a set of "random" data, ordered from smallest to largest, which follows a normal distribution
# Works by defining a set of "bins" then setting limits of integration to the upper and lower bound of the bin
# Function will integrate the normal distribution, which returns the proportion of total data that should be in the bin
def generateNormalData(nbins, min, max, number, mean, std):
    detail = (max - min) / nbins
    lower = min
    upper = min + detail
    data = []
    while upper <= max + detail:
        integral = quad(normalDist, lower, upper, args=(mean,std))
        probability = integral[0]
        for p in range(int(round(probability*number))):
            data.append(random.uniform(lower,upper))
        lower += detail
        upper += detail
    return data

# Generates a set of "random" data, ordered from smallest to largest, which follows a skewed distribution
# Works by defining a set of "bins" then setting limits of integration to the upper and lower bound of the bin
# Function will integrate the skewed distribution, which returns the proportion of total data that should be in the bin
# Known problem: Because the integrals form very small floating points which become rounded and converted to integers, the final dataset is not exactly as long as specified.
def generateSkewData(nbins, min, max, number, mean=0, std=1,scale=1,skew=5,loc=0):
    detail = (max - min) / nbins
    lower = min
    upper = min + detail
    data = []
    while upper < max + detail:
        integral = quad(skewedDist, lower, upper, args=(loc,scale,skew,mean,std))
        probability = integral[0]
        for p in range(int(round(probability*number))):
            data.append(random.uniform(lower,upper))
        lower += detail
        upper += detail
    return data

# Will generate a list of probabilities as long as "nbins." Follows the normal distribution.
# Useful for generating single data points that fit in the distribution.
def generateNormalProb(nbins, min, max, mean, std):
    detail = (max - min) / nbins
    lower = min
    upper = min + detail
    probs = []
    while upper < max+detail:
        integral = quad(normalDist, lower, upper, args=(mean,std))
        probs.append(integral[0])
        lower += detail
        upper += detail
    return probs

# Will generate a list of probabilities as long as "nbins." Follows the skewed distribution.
# Useful for generating single data points that fit in the distribution.
def generateSkewProb(nbins, min, max, mean=0, std=1,scale=1,skew=5,loc=0):
    detail = (max - min)/nbins
    lower = min
    upper = min + detail
    probs = []
    while upper < max + detail:
        integral = quad(skewedDist, lower, upper, args=(loc,scale,skew,mean,std))
        probs.append(integral[0])
        lower += detail
        upper += detail
    return probs

list = generateSkewProb(100,-3,1,0,.50,1.18,6.7,-2.1)
print(list)
print(len(list))
print(sum(list))