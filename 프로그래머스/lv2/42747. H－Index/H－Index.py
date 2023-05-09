def solution(citations):
    answer = 0
    for h in range(len(citations)+1): 
        over_h = [c for c in citations if c>=h]
        if len(over_h)>=h: 
            answer =h
    return answer