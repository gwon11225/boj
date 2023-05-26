word = input()
arr = []
for i in range(len(word)):
    arr.append(word[i])
    if len(arr) >= 4:
        if arr[-4:] == ['P','P','A','P']:
            arr.pop()
            arr.pop()
            arr.pop()
            arr.pop()
            arr.append('P')
if arr == ['P']:
    print("PPAP")
else:
    print("NP")