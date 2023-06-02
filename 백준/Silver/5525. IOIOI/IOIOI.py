n = int(input())
word_len = int(input())
word = input()
arr_i = [i for i in range(word_len - 2) if word[i:i+3] == "IOI"]
check = "I" + "OI"*n
count = 0
for i in range(len(arr_i) - n + 1):
    if word[arr_i[i]:arr_i[i] + n*2 + 1] == check:
        count += 1
print(count)