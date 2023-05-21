from math import lcm
from math import gcd
a_1,a_2 = map(int,input().split())
b_1,b_2 = map(int,input().split())
l = lcm(a_2,b_2)
a_2 = l//a_2
b_2 = l//b_2
g = gcd(a_1*a_2+b_1*b_2,l)
print((a_1*a_2+b_1*b_2)//g,l//g)