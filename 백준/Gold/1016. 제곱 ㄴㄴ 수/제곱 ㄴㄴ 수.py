minimum,maximum = map(int,input().split())
arr = [1 for _ in range(maximum - minimum + 1)]
i = 2
while i**2 <= maximum:
    mul = minimum // i**2
    while mul * (i ** 2) <= maximum:
        if 0 <=  mul * (i ** 2) - minimum <= maximum - minimum:
            arr[mul * (i ** 2) - minimum] = 0
        mul += 1
    i += 1
print(sum(arr))