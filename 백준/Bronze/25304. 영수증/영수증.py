sum_cost = int(input())
n = int(input())
sum = 0
for i in range(n):
    cost,num = map(int,input().split())
    sum += cost*num
if sum_cost == sum:
    print("Yes")
else:
    print("No")