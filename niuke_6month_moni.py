import math
s = 6




def _find(s):
    if s == 1:
        return 1
    if s == 2:
        return 2
    if isPrime(s) == 0:
        return 2 * _find(s-1)
    else:
        if s / isPrime(s) != isPrime(s):
            return _find(s-1)
        else:
            return 2 * _find(s-1) - _find(isPrime(s))

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return 0

print(_find(5) % 1000000007)





