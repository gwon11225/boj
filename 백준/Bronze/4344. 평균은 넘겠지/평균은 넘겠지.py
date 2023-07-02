import sys
input=sys.stdin.readline
a = int(input())

for j in range(a):
    b = list(map(int,input().split()))
    count = 0
    sum = 0
    for k in range(1,len(b)):
        sum += b[k]
    avr = sum / b[0]
    for i in range(1,len(b)):
        if b[i] > avr:
            count += 1
    dd = count / b[0] * 100
    print(round(dd,3),"%",sep="")