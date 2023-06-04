n = int(input())
word = str(bin(n + 1))[3:]
for i in word:
    if i == '0':
        print(4,end="")
    else:
        print(7,end="")