count, i = 0, 3
arr = [2]

while count != 10000:
    isPrime = True
    for num in arr:
        if i % num == 0:
           isPrime = False 
           break
    if isPrime:
        arr.append(i)
        count += 1
    i += 1

print(arr[-1])
