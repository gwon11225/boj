from math import factorial
a,b = map(int,input().split())
answer = factorial(a) // factorial(b) // factorial(a-b)
print(answer)