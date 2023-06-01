word = input()
answer = 0
if 'A' in word:
    answer += 4
elif 'B' in word:
    answer += 3
elif 'C' in word:
    answer += 2
elif 'D' in word:
    answer += 1

if "+" in word:
    answer += 0.3
elif "-" in word:
    answer -= 0.3
print(float(answer))