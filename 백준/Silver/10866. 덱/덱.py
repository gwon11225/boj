from sys import stdin
n = int(stdin.readline().rstrip())
arr = []
for i in range(n):
    word = stdin.readline().rstrip().split()
    if len(word) == 1:
        if word == ["front"]:
            print(arr[0] if len(arr) != 0 else -1)
        elif word == ["back"]:
            print(arr[-1] if len(arr) != 0 else -1)
        elif word == ["size"]:
            print(len(arr))
        elif word == ["empty"]:
            print(1 if len(arr) == 0 else 0)
        elif word == ["pop_back"]:
            if len(arr) == 0:
                print(-1)
            else:
                print(arr[-1])
                arr.pop()
        elif word == ["pop_front"]:
            if len(arr) == 0:
                print(-1)
            else:
                print(arr[0])
                arr.pop(0)
    else:
        if word[0] == "push_back":
            arr.append(word[1])
        else:
            arr.insert(0, word[1])