# 문자열 탐색 알고리즘
# kmp 알고리즘

#테이블 생성
def make_table(sentence: str):
    length = len(sentence)
    table = [0 for _ in range(length)]
    i = 0

    for j in range(1, length):
        while i > 0 and sentence[i] != sentence[j]:
            i = table[i - 1]
        
        if sentence[i] == sentence[j]:
            i += 1
            table[j] = i

    return table

result = []

sentence = input()
pattern = input()

table = make_table(pattern)
i = 0
for j in range(len(sentence)):
    while i > 0 and pattern[i] != sentence[j]:
        i = table[i - 1]

    if pattern[i] == sentence[j]:
        i += 1
        if i == len(pattern):
            result.append(j - i + 2)
            i = table[i - 1]

print(len(result))
print(*result)