def solution(s):
    arr = []
    for i in s:
        if i == '(': arr.append(i)
        elif len(arr) != 0: arr.pop()
        else: return False

    return True if len(arr) == 0 else False