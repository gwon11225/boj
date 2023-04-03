from math import gcd
while True:
    try:
        n = input()
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
        print("%s = %.0f / %.0f" %(n,real_float/max,real_length/max))
    except:
        break