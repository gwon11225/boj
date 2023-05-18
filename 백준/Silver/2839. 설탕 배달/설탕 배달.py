n = int(input())
a = n//5
while True:
    if (n - a*5)%3 == 0:
        print(a+(n - a*5)//3)
        exit()
    else:
        a -= 1
    if a < 0:
        break
print(-1)