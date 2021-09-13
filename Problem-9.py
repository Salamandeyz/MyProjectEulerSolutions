for i in range(1, 1000):
    A = 1000 - i
    if 500000 % A == 0 and 500000 // A < 1000:
        b = 1000 - (500000 // A)
        a = 1000 - A
        c = 1000 - a - b
        break

ans = a*b*c 
print(ans)


