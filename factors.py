#!/usr/bin/python3

import sys

def factorize(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return (i, n // i)
        i += 1
    return (n, 1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: factors <file>')
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        for line in f:
            n = int(line.strip())
            p, q = factorize(n)
            print(f'{n}={p}*{q}')

