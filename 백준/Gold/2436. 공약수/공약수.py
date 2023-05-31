from math import gcd,lcm
a,b = map(int, input().split())
s = a*b
arr = []
for i in range(a,int(s ** 0.5) + 1,a):
    if gcd(i, s//i) == a and lcm(i, s//i) == b:
        arr.append([i, s//i, i + (s//i)])
arr.sort(key= lambda x: x[2])
print(arr[0][0],arr[0][1])