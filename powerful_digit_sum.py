max = 0

for i in range(1, 100):
    for j in range(1, 100):
        product = str(i**j)
        sum = 0
        for digit in product:
            sum += int(digit)
        if sum > max:
            max = sum

print(max)

