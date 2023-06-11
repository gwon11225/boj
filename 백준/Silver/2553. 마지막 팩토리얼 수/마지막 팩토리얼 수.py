from math import factorial
s = list(str(factorial(int(input()))))
s.reverse()
s = int(''.join(s))
print(str(s)[0])