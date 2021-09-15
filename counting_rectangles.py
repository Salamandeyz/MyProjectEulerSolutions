min = 2000000
for i in range(2830):
    for j in range(i, 2830):
        temp = j*i*(j+1)*(i+1) // 4
        diff = abs(2000000 - temp)
        if diff < min:
            min = diff 
            ans = i*j 

print(ans)

