A = int(input())
B = input()
C = list(B)
for i in range(A):
    C[i] = int(C[i])
print(sum(C))