def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for _ in range(len(A)):
        answer += A.pop(0) * B.pop()

    return answer