from sys import stdin
n = int(stdin.readline().rstrip())
word_len = int(stdin.readline().rstrip())
word = stdin.readline().rstrip()
check = 'I' + 'OI'*n
cnt = 0
arr = []
i = 0
while word_len != i:
    if i <= word_len - n*2+1:
        if word[i:i + n*2 + 1] == check:
            cnt += 1
            i += 2
            continue
    i += 1
print(cnt)