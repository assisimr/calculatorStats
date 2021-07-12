import math
from Statistics.variance import variance

def std_dev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev
