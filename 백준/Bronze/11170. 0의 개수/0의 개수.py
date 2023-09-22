n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    summ = 0
    for i in range(a, b + 1):
        summ += str(i).count('0')
    print(summ)