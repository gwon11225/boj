def solution(s):
    answer = [s[0].upper()]
    for i in list(s[1:]):
        if answer[-1] == ' ':
            answer.append(i.upper())
        else:
            answer.append(i.lower())
    return ''.join(answer)