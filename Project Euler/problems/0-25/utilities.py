# Utility functions for Project Euler
# - - -
# Walter Sagehorn

import math, time

## helper method for n_primes
def is_prime(num, l):
    for i in l:
        if (num % i == 0):
            return False
        if (i > math.sqrt(num)):
            return True
    return True

## calculates n prime numbers
def n_primes(n):
    l = [2,3,5,7]
    i = 11
    if n < 5:
        return l[:n]
    while (len(l) < n):
        if is_prime(i, l):
            l.append(i)
        i += 2
    return l

def primes_below(x):
    l = [2]
    i = 3
    if x < 3: return []
    while (i < x):
        if is_prime(i, l):
            l.append(i)
        i += 2
    return l

# TODO: better prime algorithm