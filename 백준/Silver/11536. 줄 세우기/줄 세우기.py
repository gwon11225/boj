arr = [input() for _ in range(int(input()))]
if arr == sorted(arr):
    print("INCREASING")
elif arr == sorted(arr,reverse=True):
    print("DECREASING")
else:
    print("NEITHER")