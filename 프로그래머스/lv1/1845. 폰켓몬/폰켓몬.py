def solution(nums):
    answer = len(set(nums))
    s = len(nums)//2
    if answer < s:
        return answer
    else:
        return s