from math import ceil

sumDiv_3 = sum([3*i for i in range(ceil(1000/3))])
sumDiv_5 = sum([5*i for i in range(ceil(1000/5))])
sumDiv_15 = sum([15*i for i in range(ceil(1000/15))])

ans = sumDiv_3 + sumDiv_5 - sumDiv_15
print(ans)
