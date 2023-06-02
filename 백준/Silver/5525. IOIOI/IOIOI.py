n = int(input())
word_len = int(input())
word = input()
check = 'I'
for _ in range(n):
    check += 'OI'
cnt = 0
arr = []
for i in range(word_len):
    arr.append(word[i])
    if 1+n*2 <= len(arr):
        if arr[-(n*2+1):] == list(check):
            cnt += 1
print(cnt)