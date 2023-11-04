from itertools import combinations
def solution(number):
    answer = 0
    temp = combinations(number, 3)
    # print(temp)
    for t in temp:
        # print(t, sum(t))
        if sum(t)==0:
            answer += 1
    return answer