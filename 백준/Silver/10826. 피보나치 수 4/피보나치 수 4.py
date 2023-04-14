n = int(input())
if n == 0:
    print(0)
    exit()
fibo = [1,1]
for i in range(2,n+1):
    fibo.append(fibo[i-2] + fibo[i-1])
print(fibo[-2])