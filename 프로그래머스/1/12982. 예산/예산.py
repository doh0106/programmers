def solution(d, budget):
    answer = 0
    d.sort()
    # print(d)
    idx = 0 
    for _ in range(len(d)):
        answer += d[idx]
        if answer > budget:
            # print(answer, 'out')
            break
        idx += 1        
    return idx