from sys import stdin
while True:
    word = stdin.readline().rstrip()
    if word == '0':
        break
    if word == word[::-1]:
        print("yes")
    else:
        print("no")