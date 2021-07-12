from Calculator.addition import addition
from Calculator.division import division

def median(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = addition(total, num)

    if num_values % 2 == 0:
        median1 = data[num_values // 2]
        median2 = data[num_values // 2 - 1]
        Median = (median1 + median2) / 2
    else:
        Median = division(num_values, 2)

    return Median




