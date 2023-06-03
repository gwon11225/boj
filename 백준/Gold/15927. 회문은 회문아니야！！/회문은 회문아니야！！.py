word = input()
if word.count(word[0]) == len(word):
    print(-1)
elif word[::-1] == word:
    print(len(word) - 1)
else:
    print(len(word))