import math

PI = 3.141592653589793
E = 2.718281828459045

def abs_val(x):
    return x if x >= 0 else -x

def power(base, exp):
    if exp == int(exp) and exp >= 0:
        result = 1
        for _ in range(int(exp)):
            result *= base
        return result
    if base <= 0:
        raise ValueError("Отрицательное основание с дробной степенью")
    return exp(exp * ln(base))

def sqrt(x):
    if x < 0:
        raise ValueError("Корень из отрицательного числа")
    if x == 0:
        return 0.0
    guess = x / 2.0
    for _ in range(100):
        new_guess = (guess + x / guess) / 2.0
        if abs_val(new_guess - guess) < 1e-15:
            break
        guess = new_guess
    return guess

def exp(x, terms=50):
    result = 1.0
    term = 1.0
    for n in range(1, terms):
        term *= x / n
        result += term
    return result

def ln(x, terms=1000):
    if x <= 0:
        raise ValueError("Логарифм определён только для x > 0")
    z = (x - 1) / (x + 1)
    result = 0.0
    for n in range(terms):
        result += z ** (2 * n + 1) / (2 * n + 1)
    return 2 * result

def log(x, base=E):
    return ln(x) / ln(base)

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факториал только для неотрицательных целых")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def gcd(a, b):
    a, b = abs_val(a), abs_val(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs_val(a * b) // gcd(a, b)

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True