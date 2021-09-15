from data.names_data import names

names = sorted(names)

sum, i = 0, 1
for name in names:
    score = 0
    for char in name:
        score += "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char) + 1
    sum += i*score
    i += 1

print(sum)

    
