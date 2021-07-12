from Calculator.addition import addition
from Calculator.division import division
from Statistics.mean import mean
from Statistics.getSample import getSample


def sample_mean(data, sample_size):
    total = 0

    sample = getSample(data, sample_size)
    num_values = len(sample)
    for num in sample:
        total = addition(total, num)
    return division(total, num_values)

def sample_median(data, sample_size):
    total = 0

    sample = getSample(data, sample_size)
    num_values = len(sample)
    for num in sample:
        total = addition(total, num)
    return division(total, num_values)

def sample_mode(data, sample_size):

    sample = getSample(data, sample_size)
    num_values = sample
    return max(num_values)

def sample_variance(data, sample_size):

    sample = getSample(data, sample_size)
    n = len(sample)
    Mean = sum(data) / n
    deviations = [(x - Mean) ** 2 for x in data]
    Variance = sum(deviations) / n
    return Variance
