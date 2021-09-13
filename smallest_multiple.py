from functools import reduce

def lcm(a, b):
    A, B = a, b
    while B != 0:
        A, B = B, A % B

    return (a*b) // A

ans = reduce(lcm, list(range(1, 21)))
print(ans)
