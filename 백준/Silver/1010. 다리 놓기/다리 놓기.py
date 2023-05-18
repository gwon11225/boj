import sys
def fact(a):
    ans = 1
    for i in range(1,a+1):
        ans *= i
    return ans

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
answer = 1
for i in arr:
    answer = (fact(i[1])//fact(i[0]))//fact(i[1]-i[0])
    print(answer)