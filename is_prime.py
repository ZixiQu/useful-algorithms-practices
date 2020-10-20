def is_prime(k):
    for d in range(2, k):
        if k % d ==0:
            return False
    return True

def get_primes(n):
    """ find every prime number from 1 to n"""
    result = []
    for k in range(2, n+1):
        if is_prime(k):
            result.append(k)
    return result
