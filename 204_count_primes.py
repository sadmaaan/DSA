def countPrimes(n):        
        primes = [False, False] + [True] * (n - 2)
        print(count_primes(n, primes))
    
def count_primes(n, primes):
    i = 2
    while i * i < n:
        if primes:
            j = 2 * i
            while j < n:
                primes[j] = False
                j += i
        i += 1
    
    return sum(primes)

print(countPrimes(40))