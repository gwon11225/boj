h,m = map(int,input().split())
later = int(input())
if m + later >= 60:
    h += (m+later)//60
    m = (m+later)%60
    if h >= 24:
        h -= 24
else:
    m += later
print(f"{h} {m}")