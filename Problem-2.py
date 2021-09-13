a, b = 1, 2
ans = 0

while b < 4000000:
    ans += b
    for _ in range(3):
        a, b = b, a+b

print(ans)
    
