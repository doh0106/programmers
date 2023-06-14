def solution(dartResult):
    answer = []
    darts = [] 
    bonus_dic = dict(zip(['S', 'D', 'T'], [1, 2, 3]))
    for _ in range(3): 
        point, bonus, option = '', '', ''
        idx = 0
        for _ in range(len(dartResult)): 
            if dartResult[idx].isnumeric(): 
                point += dartResult[idx]
                idx += 1
            else: 
                break 
        for _ in range(len(dartResult)): 
            try:
                if not dartResult[idx].isnumeric():
                    bonus += dartResult[idx]
                    idx+=1
                else: 
                    break
            except: 
                pass
        if len(bonus)==2: 
            option = bonus[-1]
            bonus = bonus[0]
        if option:
            darts.append([point, bonus, option])
        else:
            darts.append([point, bonus])
        dartResult=dartResult[idx:]
    for d in darts: 
        if len(d)==2: 
            answer.append(int(d[0])**bonus_dic[d[1]])
        elif len(d)==3: 
            if d[-1]=='#': 
                answer.append(-int(d[0])**bonus_dic[d[1]])
            else: 
                if answer: 
                    answer[-1]*=2 
                    answer.append(2*int(d[0])**bonus_dic[d[1]])
                else: 
                    answer.append(2*int(d[0])**bonus_dic[d[1]]) 
    return sum(answer)