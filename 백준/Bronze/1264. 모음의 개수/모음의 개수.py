arr = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
while True:
    cnt = 0
    word = input()
    if word == '#':
        break
    for i in word:
        if i in arr:
            cnt += 1
    print(cnt)