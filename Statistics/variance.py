

def variance(data):
    n = len(data)
    Mean = sum(data) / n
    deviations = [(x -  Mean) ** 2 for x in data]
    Variance = sum(deviations) / n
    return Variance


