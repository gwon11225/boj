word = list(input())
find = list(input())
arr = []
cnt = 0
for i in word:
    arr.append(i)
    if arr[-len(find):] == find:
        for j in range(len(find)):
            arr.clear()
        cnt += 1
print(cnt)