import math
from functools import reduce

def ekub(a, b):
    return math.gcd(a, b)

def ekuk(a, b):
    return a * b // math.gcd(a, b)

def ekub3(a, b, c):
    return reduce(math.gcd, [a, b, c])

def ekuk3(a, b, c):
    def lcm(x, y):
        return x * y // math.gcd(x, y)
    return reduce(lcm, [a, b, c])

def nbs(n):
    return len([i for i in range(1, n+1) if n % i == 0])

def ubs(a, b):
    return len(set(i for i in range(1, min(a, b)+1) if a % i == 0 and b % i == 0))

def nby(n):
    return sum(i for i in range(1, n+1) if n % i == 0)
