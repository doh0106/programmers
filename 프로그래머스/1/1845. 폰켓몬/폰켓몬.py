def solution(nums):
    answer = 0
    temp = list(set(nums))
    if len(nums)//2 > len(temp):
        return len(temp)
    else:
        return len(nums)//2
