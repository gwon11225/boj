arr = list(map(int,input().split()))
year = [1,1,1]
cnt = 0
while year != arr:
    for i in range(3):
        year[i] += 1
    if year[0] > 15:
        year[0] = 1
    if year[1] > 28:
        year[1] = 1
    if year[2] > 19:
        year[2] = 1
    cnt += 1
print(cnt + 1)