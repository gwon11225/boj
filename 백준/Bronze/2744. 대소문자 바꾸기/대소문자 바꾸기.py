word = list(input())
answer = []
for i in word:
    if ord("A") <= ord(i) <= ord("Z"):
        answer.append(chr(ord(i) + 32))
    elif ord("a") <= ord(i) <= ord("z"):
        answer.append(chr(ord(i) - 32))
print(''.join(answer))