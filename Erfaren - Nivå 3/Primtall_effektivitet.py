from math import sqrt, ceil

def eratosthenes(max):
    candidates = [True] * max
    candidates[0] = False
    candidates[1] = False

    for i in range(2, int(max**0.5) + 1):
        if candidates[i]:
            for j in range(i**2, max, i):
                candidates[j] = False

    primes = []
    for i in range(max):
        if candidates[i]:
            primes.append(i)
    return primes

def is_prime(n, small_primes=[2, 3, 5]):
    if not (isinstance(n, int) and n > 1): 
        return False
    if n in small_primes:
        return True
    for prime in small_primes:
        if n % prime == 0:
            return False
    start = small_primes[-1] + 2
    for i in range(start, ceil(sqrt(n)), 2):
        if is_prime(i):
            if n % i == 0:
                return False
    return True

upper_bound = 1000000
small_primes = eratosthenes(upper_bound)

print(is_prime(15, small_primes))
print(is_prime(29, small_primes))
print(is_prime(2147483647, small_primes))


#print(is_prime(15))
#print(is_prime(29))
#print(is_prime(2147483647))

