n = int(input())
i = 1
if n == 1:
    print(f"{n}/{i}")
    exit()
while n > i:
    n -= i
    i += 1
if i % 2 == 0:
    print(f"{n}/{i+1-n}")
else:
    print(f"{i+1-n}/{n}")