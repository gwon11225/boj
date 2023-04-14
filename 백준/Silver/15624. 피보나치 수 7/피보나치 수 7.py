fibo_first = 1
fibo_second = 1
fibo = 0
n = int(input())
if n == 1:
    print(1)
    exit()
if n == 2:
    print(1)
    exit()
for i in range(n - 2):
    fibo = fibo_first%1000000007 + fibo_second%1000000007
    fibo_first = fibo_second%1000000007
    fibo_second = fibo
print(fibo)