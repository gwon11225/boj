num,jin = map(int,input().split())
arr = []
while num:
    if num%jin >= 10:
        arr.append(chr(num%jin+55))
    else:
        arr.append(num%jin)
    num //= jin
arr.reverse()
print(''.join(map(str,arr)))