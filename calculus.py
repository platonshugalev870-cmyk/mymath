def derivative(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

def second_derivative(f, x, h=1e-4):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)

def integrate(f, a, b, n=1000):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        total += (4 if i % 2 else 2) * f(x)
    return total * h / 3

def gradient(f, point, h=1e-6):
    grad = []
    for i in range(len(point)):
        p_plus = list(point); p_plus[i] += h
        p_minus = list(point); p_minus[i] -= h
        grad.append((f(*p_plus) - f(*p_minus)) / (2 * h))
    return grad