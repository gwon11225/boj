a = input()
b = a.split()
c = b[0].strip()
d = b[1].strip()

num_1 = [int(c[0]),int(c[1]),int(c[2])]
num_2 = [int(d[0]),int(d[1]),int(d[2])]
    
result_1 = num_1[2]*100 + num_1[1]*10 + num_1[0]
result_2 = num_2[2]*100 + num_2[1]*10 + num_2[0]


if result_1 > result_2:
    print(result_1)
elif result_1 < result_2:
    print(result_2)