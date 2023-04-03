n = int(input())
left = 0
right = n  - 3

if n == 1:
    print("*")
    exit()

print("*"*n)
for i in range(n-2):
    print("*",end="")
    for j in range(n - 2):
        if j == left or j == right:
            print("*",end="")
        else:
            print(" ",end="")
    print("*")
    left += 1
    right -= 1
print("*"*n)