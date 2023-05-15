def solution(genres, plays):
    answer = []
    g_dic = {}
    for g, p in zip(genres, plays): 
        if g not in g_dic: 
            g_dic[g] = p
        else: 
            g_dic[g] += p
    temp = [[g, p, idx] for idx, (g, p) in enumerate(zip(genres, plays))]   
    temp.sort(reverse=True, key = (lambda x : (g_dic[x[0]], x[1], -x[2])))
    count_dic = {k:0 for k in g_dic.keys()}
    for g, p, idx in temp:
        if count_dic[g]<2: 
            answer.append(idx)
            count_dic[g]+=1
        else: 
            pass
        # pass
    return answer