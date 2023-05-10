def solution(k, tangerine):
    answer = 0
    dic = {k:0 for k in set(tangerine)}
    for i in tangerine:
        dic[i]+=1
    arr = sorted([(i,j) for (i,j) in dic.items()], key=lambda x: x[1], reverse=True)
    count = 0 
    for (x,y) in arr: 
        count += y
        answer+=1
        if count>=k:
            break
    return answer