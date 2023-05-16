def solution(N, stages):
    answer = []
    s_dic = {k:0 for k in range(1, N+1)}
    for i in stages: 
        if i>N: 
            s_dic[i-1] += 1
        else: 
            s_dic[i]+=1
            
    for k,v in s_dic.items(): 
        for x in range(k+1, N+1): 
            s_dic[k]+=s_dic[x]
    
    for i in range(1, N+1): 
        if s_dic[i]!=0:
            answer.append([i, stages.count(i)/s_dic[i]])
        else: 
            answer.append([i,0 ])
    answer.sort(key=lambda x:(-x[1], x[0]))
    return [i[0] for i in answer]