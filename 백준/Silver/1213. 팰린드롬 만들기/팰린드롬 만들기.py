word = list(input())
dct = {}
cnt = 0
for i in set(word):
    dct[i] = word.count(i)
dct = sorted(list(dct.items()),key=lambda x:x[0])
odd = 0
for i in range(len(dct)):
    if dct[i][1]%2 != 0:
        cnt += 1
        odd = dct[i][0]
if cnt >= 2:
    print("I'm Sorry Hansoo")
else:
    for i in dct:
        print(i[0] * (i[1]//2),end="")
    if cnt == 1:
        print(odd, end="")
    dct.reverse()
    for i in dct:
        print(i[0] * (i[1]//2),end="")