from data.p059_cipher import cipher
from itertools import combinations, permutations

for combo in permutations('abcdefghijklmnopqrstuvwxyz', 3):
    text = ""
    i = 0
    for num in cipher:
        text += chr(num ^ ord(combo[i % 3]))
        i += 1
    if 'he' in text and 'will' in text and 'the' in text and 'is' in text and 'by' in text:
        key = combo # 'exp'

sum, i = 0, 0
for num in cipher:
    sum += num ^ ord(key[i % 3])
    i += 1

print(sum)
