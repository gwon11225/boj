a,b,c = map(int,input().split())
money = 0
if a == b and a == c and b == c:
    money += 10000 + a*1000
elif a == b or a == c or b == c:
    if a == b:
        money += 1000 + a*100
    elif a == c:
        money += 1000 + a*100
    else:
        money += 1000 + b*100
else:
    if a > b and a > c:
        money += a*100
    elif b > a and b > c:
        money += b*100
    else:
        money += c*100
print(money)