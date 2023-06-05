from math import factorial
n = int(input())
s = str(factorial(n))
cnt = 0
for i in range(len(s)-1,-1,-1):
    if s[i] != '0':
        break
    cnt += 1
print(cnt)