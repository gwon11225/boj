word = [0 for _ in range(5)]
max = 0
for i in range(5):
    word[i] = list(input())
for i in range(5):
    if len(word[i]) > max:
        max = len(word[i])
for i in range(max):
    for j in range(5):
        try:
            print(word[j][i],end="")
        except:
            continue