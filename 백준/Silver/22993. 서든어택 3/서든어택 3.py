n = int(input())
arr = list(map(int,input().split()))
first = arr[0]
ar = sorted(arr[1:])
answer = 'Yes'
for i in ar:
    if first > i:
        first += i
    else:
        answer = 'No'
print(answer)