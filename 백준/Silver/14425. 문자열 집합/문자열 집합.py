a,b = map(int,input().split())
st = set()
arr = []
cnt = 0
for i in range(a):
    st.add(input())
for i in range(b):
    arr.append(input())
for i in arr:
    if i in st:
        cnt += 1
print(cnt)