import sys 
s = sys.stdin.readline().strip()
s = list(s)
abc_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
k = [-1]*(len(abc_list))
for i in range(26):
    if abc_list[i] in s:
        k[i] = s.index(abc_list[i])

print(*k, sep=' ')