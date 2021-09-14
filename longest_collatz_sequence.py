temp, ans = 0, 0

for i in range(1, 1_000_000):
    count = 0
    n = i
    while n > 1:
        count += 1
        if n % 2 == 0: n = n // 2
        else: n = 3*n + 1
    if count > temp:
        temp = count
        ans = i

print(ans)
