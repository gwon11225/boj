word = input()
if len(word) == 1:
    print(1)
    exit()
word_2 = word
first = 0
end = len(word) - 1
for i in range(len(word)//2):
    check_word = ''
    for j in range(len(word)):
        if j == first:
            check_word += word_2[end]
        elif j == end:
            check_word += word_2[first]
        else:
            check_word += word_2[j]
    first += 1
    end -= 1
    word_2 = check_word
if word_2 == word:
    print(1)
else:
    print(0)