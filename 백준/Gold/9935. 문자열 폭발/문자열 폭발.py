word = list(input())
bomb = list(input())
arr = []
b_len = len(bomb)
for i in range(len(word)):
    arr.append(word[i])
    if arr[-b_len:] == bomb:
        for j in range(b_len):
            arr.pop()
if len(arr) == 0:
    print("FRULA")
else:
    print(''.join(arr))