length = 0
lst = []

with open("data/triangle1.txt", "r") as file:
    for line in file:
        length += 1
        lst.append(list(map(int, line.split())))

lst = list(reversed(lst))
for i in range(length - 1):
    for j in range(length - i - 1):
        lst[i+1][j] += max(lst[i][j], lst[i][j+1])

ans = lst[-1][0]
print(ans)
