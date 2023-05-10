def solution(n):
    answer = n + 1
    a = bin(n)[2:].count('1')
    while True: 
        c = bin(answer)[2:].count('1')
        # print(a, c, answer)
        # break
        if a==c: 
            break 
        answer +=1
    return answer