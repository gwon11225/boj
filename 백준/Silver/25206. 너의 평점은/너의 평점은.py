sum = 0.0
sum_cls = 20
sum_score = 0.0
for i in range(20):
    class_name,score,level = input().split()
    score = float(score)
    if level == 'P':
        sum_cls -= 1
        continue
    sum += score
    if level == 'A+':
        sum_score += 4.5*score
    elif level == 'A0':
        sum_score += 4.0*score
    elif level == 'B+':
        sum_score += 3.5*score
    elif level == 'B0':
        sum_score += 3.0*score
    elif level == 'C+':
        sum_score += 2.5*score
    elif level == 'C0':
        sum_score += 2.0*score
    elif level == 'D+':
        sum_score += 1.5*score
    elif level == 'D0':
        sum_score += 1.0*score
    else:
        continue
print(f"{format(sum_score/sum,'.6f')}")