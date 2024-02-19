def check(f: list, s: list):
    cnt = 0
    for i in range(8):
        if f[i] != s[i]: cnt += 1

    return cnt

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

answer = []

first = [
    list("WBWBWBWB"),
    list("BWBWBWBW")
] * 4

second = [
    list("BWBWBWBW"),
    list("WBWBWBWB")
] * 4

for i in range(m - 7):
    for j in range(n - 7):
        cnt = 0
        for k in range(8):
            cnt += check(arr[j + k][i : i + 8], first[k])
        answer.append(cnt)
        cnt = 0
        for k in range(8):
            cnt += check(arr[j + k][i : i + 8], second[k])
        answer.append(cnt)
print(min(answer))