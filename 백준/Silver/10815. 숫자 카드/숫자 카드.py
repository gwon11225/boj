n = int(input())
arr = set(map(int,input().split()))
m = int(input())
answer = list(map(int,input().split()))
for i in answer:
    if i in arr:
        print(1,end=" ")
    else:
        print(0,end=" ")