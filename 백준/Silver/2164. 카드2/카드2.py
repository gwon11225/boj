n = int(input())

head = n - 1
leaf = 0

def pop(arr):
    global leaf
    leaf += 1
    return arr[leaf - 1]


arr = [i for i in range(1, n + 1)]


for i in range(n - 1):
    pop(arr)
    arr.append(pop(arr))
    
print(arr[-1])