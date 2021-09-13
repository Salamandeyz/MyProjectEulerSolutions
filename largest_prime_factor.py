from math import sqrt

def isPrime(n):
    if n == 1: return False
    if n == 2: return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(1, int(sqrt(600851475143))):
    if 600851475143 % i == 0 and isPrime(i):
        ans = i

print(ans)
