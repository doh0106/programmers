def solution(date1, date2):
    y1,m1,d1 = date1
    y2,m2,d2 = date2
    if y2>y1:
        answer= 1
    elif y2==y1: 
        if m2>m1: 
            answer= 1
        elif m2==m1:
            if d2>d1:
                answer= 1
            else:
                answer= 0 
        elif m2<m1:
            answer= 0                          
    elif y1>y2:
        answer= 0
    return answer
