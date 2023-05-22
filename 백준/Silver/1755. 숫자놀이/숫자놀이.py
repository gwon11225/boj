m,n = map(int,input().split())
dct = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
arr = []
cnt = 0
for i in range(m,n+1):
    a = ''
    for j in str(i):
        a += dct[int(j)]
    arr.append([a,i])
arr.sort(key= lambda x:x[0])
for i in range(1,n-m+2):
    print(arr[i - 1][1],end=" ")
    cnt += 1
    if cnt%10 == 0:
        print()