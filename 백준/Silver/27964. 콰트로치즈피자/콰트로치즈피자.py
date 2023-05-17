n = int(input())
arr = list(input().split())
cnt = 0
check = []
for i in arr:
    if len(i) < 6:
        continue
    else:
        if i[-6:] == "Cheese":
            if i not in check:
                check.append(i)
                cnt += 1
if cnt >= 4:
    print("yummy")
else:
    print("sad")