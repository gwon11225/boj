a = input()
b = a.split()
c = a.strip()
count = 0
for i in b:
    if i == ' ':
        count = count + 1



if count == len(b):
    print('0')
else:
    print(len(b) - count)