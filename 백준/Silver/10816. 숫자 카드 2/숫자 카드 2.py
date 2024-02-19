n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

answer = [0] * 20000001

for i in arr:
    answer[i + 10000000] += 1

for i in arr2:
    print(answer[i + 10000000], end=" ")