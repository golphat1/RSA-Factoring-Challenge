#!/usr/bin/python3

import sys
import math

def isqrt(n):
    # Return the integer square root of n.
    return math.isqrt(n)

def ceil_sqrt(n):
    # Return the ceiling of the square root of n.
    return math.isqrt(n) + (1 if math.isqrt(n) ** 2 != n else 0)

def find_factors(n):
    a = ceil_sqrt(n)
    b = ceil_sqrt(a ** 2 - n)
    k = 1
    while True:
        t = k * b + n
        x = isqrt(t)
        y2 = x ** 2 - t
        if y2 >= 0 and isqrt(y2) ** 2 == y2:
            return (x + isqrt(y2), x - isqrt(y2))
        k += 1

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: rsa <file>')
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        for line in f:
            n = int(line.strip())
            p, q = find_factors(n)
            print(f'{n}={p}*{q}')

