def solution(operations):
    answer = []
    for i in operations:
        cmd, value = i.split()
        value = int(value)
        if cmd == "I":
            answer.append(value)
        else:
            if value == 1 and answer != []:
                answer.remove(max(answer))
            elif answer != []:
                answer.remove(min(answer))
    if len(answer) != 0:
        return [max(answer), min(answer)]
    else:
        return [0, 0]