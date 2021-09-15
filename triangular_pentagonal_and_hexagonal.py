from math import sqrt

n, i, count = 0, 1, 0

while count < 3:
    n += i
    if (sqrt(8*n + 1) + 1) % 4 == 0 and (sqrt(24*n + 1) + 1) % 6 == 0:
        count += 1
        ans = n

    i += 1

print(ans)
