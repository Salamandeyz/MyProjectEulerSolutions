sum = 0

with open("data/large_numbers.txt", 'r') as file:
    for line in file:
        sum += int(line)

ans = str(sum)[:10]
print(ans)
