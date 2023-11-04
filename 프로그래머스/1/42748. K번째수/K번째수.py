def solution(array, commands):
    answer = []
    for c in commands:
        s, e, w = c
        answer.append(sorted(array[s-1:e])[w-1])
    return answer