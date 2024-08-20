import math

arr = [int(input()) for i in range(10)]

before = 0
after = 0

for i in range(10):
    after += arr[i]

    if abs(100 - after) <= abs(100 - before):
        before += arr[i]
    else:
        print(before)
        exit()

print(after)