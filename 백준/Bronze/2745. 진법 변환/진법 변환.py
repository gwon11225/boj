import sys
word,num = sys.stdin.readline().rstrip().split()
num = int(num)
word = list(word)
sum = 0
word.reverse()
for i in range(len(word)):
    if ord(word[i]) >= 65 and ord(word[i]) <= 90:
        sum += (ord(word[i]) - ord('A') + 10)*(num**i)
    else:
        word[i] = int(word[i])
        sum += word[i]*(num**i)
print(sum)