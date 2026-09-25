from .basic import sqrt


def mean(data):
    return sum(data) / len(data)

def median(data):
    s = sorted(data)
    n = len(s)
    mid = n // 2
    if n % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    return s[mid]

def variance(data, sample=True):
    m = mean(data)
    n = len(data)
    denom = (n - 1) if sample else n
    return sum((x - m) ** 2 for x in data) / denom

def std(data, sample=True):
    return sqrt(variance(data, sample))

def covariance(x, y):
    mx, my = mean(x), mean(y)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (len(x) - 1)

def correlation(x, y):
    return covariance(x, y) / (std(x) * std(y))