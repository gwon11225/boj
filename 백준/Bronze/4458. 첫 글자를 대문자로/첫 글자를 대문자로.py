n = int(input())
for i in range(n):
    word = list(input())
    if 97 <= ord(word[0]) <= 122:
        word[0] = chr(ord(word[0])-32)
    print(''.join(word))