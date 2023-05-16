def solution(sides):
    a, b = sides
    answer = 0
    for i in range(1, sum(sides)+1): 
        temp = sorted([a, b, i])
        if sum(temp[:2]) > temp[2]:
            # print(temp)
            answer+=1
    return answer