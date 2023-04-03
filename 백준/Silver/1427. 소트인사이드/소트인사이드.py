num = input()
arr = []
for i in range(len(num)):
    arr.append(int(num[i]))
arr.sort()
for i in range(len(num)-1,-1,-1):
    print(arr[i],end="")