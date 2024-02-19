arr = []

n = int(input())

cnt = 666
while len(arr) <= n:
    if '666' in str(cnt):
        arr.append(cnt)
    cnt += 1

print(arr[-2])