def isPalindrome(n):
    temp = int(str(n)[::-1])
    if temp == n:
        return True
    return False

ans = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        if isPalindrome(i*j) and i*j > ans:
            ans = i*j

print(ans)
