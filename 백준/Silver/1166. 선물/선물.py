def can_fit(n, l, w, h, a):
    count = int(l / a) * int(w / a) * int(h / a)
    return count >= n

def find_max_a(n, l, w, h, eps=1e-7):
    left = 0.0
    right = max(l, w, h)
    
    for _ in range(100):  # 반복 횟수로 이분 탐색 정확도 보장
        mid = (left + right) / 2
        if can_fit(n, l, w, h, mid):
            left = mid  # 가능하니 더 키워보기
        else:
            right = mid  # 안 되니 줄여야 함

    return left  # right도 거의 같은 값일 것임

n, l, w, h = map(int, input().split())
print(find_max_a(n, l, w, h))