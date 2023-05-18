word = list(input().replace('9','6'))
num = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
for i in word:
    num[i] += 1
num['6'] = num['6']//2 + num['6']%2
print(max(num.values()))