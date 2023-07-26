word = input()
ans = []
for i in range(len(word)):
    ans.append(word[i:])
for i in sorted(ans):
    print(i)