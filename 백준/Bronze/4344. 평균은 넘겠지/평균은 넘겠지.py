case = int(input())

for _ in range(case):
    case_score = list(map(int,input().split()))
    score_avr = sum(case_score[1:])/case_score[0]
    count = 0
    for i in case_score[1:]:
        if i > score_avr:
            count += 1
    rate = count / case_score[0] * 100
    print(f"{rate:.3f}%")