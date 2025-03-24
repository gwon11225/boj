word = list(input())
reversed_word = list(reversed(word))
for i in range(len(word)):
    if word[i] != reversed_word[i]:
        print(0)
        exit()
        
print(1)