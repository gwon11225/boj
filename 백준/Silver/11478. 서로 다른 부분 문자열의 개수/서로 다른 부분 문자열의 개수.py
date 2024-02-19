word = input()
arr = set()

for i in range(1, len(word) + 1):
    for j in range(len(word) - i + 1):
        arr.add(word[j : j + i])

print(len(arr))