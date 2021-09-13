from math import floor, sqrt

limit = 2000000
sievebound = (limit-1)//2
sieve = [False]*sievebound
crosslimit = (floor(sqrt(limit))-1) // 2

for i in range(1, crosslimit):
    if not sieve[i]:
        for j in range(2*i*(i+1), sievebound, 2*i+1):
            sieve[j] = True

sum = 2 
for i in range(1, sievebound):
    if not sieve[i]: sum += 2*i+1

print(sum)

# This algorithm is beyond me! I just followed the step in the overview!!

