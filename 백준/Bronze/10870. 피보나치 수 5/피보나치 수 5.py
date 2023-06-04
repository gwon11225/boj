n = int(input())
if n == 0:
    print(0)
    exit()
first = 0
second = 1
for i in range(n - 1):
    second,first = first + second, second
print(second)