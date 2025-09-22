from math import sqrt, ceil
from secrets import randbelow

def is_prime(n):
    if not (isinstance(n, int) and n > 1):
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19]
    if n in small_primes:
        return True
    for prime in small_primes:
        if n % prime == 0:
            return False
    for i in range(20, ceil(sqrt(n)) + 1, 2):
        if is_prime(i):
            if n % i == 0:
                return False
    return True

#p = 23
g = 5

def generate_share(g, p):
    a = randbelow(p)
    return (a, g**a % p)

def generate_secret(other_share, a, p):
    return other_share**a % p

def find_prime(start):
    n = start
    while not is_prime(n):
        n = n + 1
    return n


#def encrypt_and_mac():
