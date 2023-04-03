from math import gcd
n = input()
for i in n:
    if i == "(":
        a,b = n.split(".")
        length = len(b) - 2
        f,loop = b.split("(")
        short_length = len(f)
        real_loop = loop.replace(")","")
        fl = float(a+"."+f+real_loop)*(10**(length))
        fl_1 = float(a+"."+f)*(10**short_length)
        real_float = fl-fl_1
        real_length = (10**length) - (10**short_length)
        max = gcd(int(real_float),int(real_length))
        print("%.0f/%.0f" %(real_float/max,real_length/max))
        exit()
try:
    word,asd = n.split(".")
    long = len(asd)
    n = float(n)
    n = n*(10**long)
    real_long = 10**long
    max = gcd(int(n),real_long)
    print(f"{int(n/max)}/{int(real_long/max)}")
except:
    print(f"{n}/1")
    exit()