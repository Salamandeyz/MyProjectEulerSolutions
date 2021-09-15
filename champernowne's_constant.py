i = 1
count = 0
nth_digit = 1
product = 1

while nth_digit <= 1000000:
    for digit in str(i):
        count += 1
        if count == nth_digit:
            product *= int(digit) 
            nth_digit *= 10
    i += 1

print(product)

