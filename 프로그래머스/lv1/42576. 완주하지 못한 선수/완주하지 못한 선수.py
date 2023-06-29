def solution(participant, completion):
    dct = {}
    sum_hash = 0
    for i in participant:
        dct[hash(i)]=i
        sum_hash += hash(i)
    for i in completion:
        sum_hash -= hash(i)
    return dct[sum_hash]