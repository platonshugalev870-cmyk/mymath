from .basic import PI, abs_val


def _normalize(x):
    x = x % (2 * PI)
    if x > PI:
        x -= 2 * PI
    return x

def sin(x, terms=20):
    x = _normalize(x)
    result = 0.0
    term = x
    for n in range(1, terms):
        result += term
        term *= -x * x / ((2 * n) * (2 * n + 1))
    return result

def cos(x, terms=20):
    x = _normalize(x)
    result = 0.0
    term = 1.0
    for n in range(1, terms):
        result += term
        term *= -x * x / ((2 * n - 1) * (2 * n))
    return result

def tan(x):
    c = cos(x)
    if abs_val(c) < 1e-15:
        raise ValueError("Тангенс не определён в этой точке")
    return sin(x) / c

def atan(x, terms=100):
    if abs_val(x) > 1:
        return (PI / 2 if x > 0 else -PI / 2) - atan(1 / x, terms)
    result = 0.0
    for n in range(terms):
        result += ((-1) ** n) * x ** (2 * n + 1) / (2 * n + 1)
    return result

def asin(x):
    if abs_val(x) > 1:
        raise ValueError("asin определён на [-1, 1]")
    if abs_val(x) == 1:
        return PI / 2 if x > 0 else -PI / 2
    return atan(x / (1 - x * x) ** 0.5)

def acos(x):
    return PI / 2 - asin(x)

def degrees_to_radians(deg):
    return deg * PI / 180

def radians_to_degrees(rad):
    return rad * 180 / PI