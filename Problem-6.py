sumSquare = sum([i*i for i in range(1, 101)])
SquaredSum = (sum(list(range(1, 101)))) ** 2

ans = SquaredSum - sumSquare
print(ans)
