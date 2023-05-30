def solution(record):
    answer = [] 
    temp = [i.split() for i in record]
    enter_dic = {'Enter' : '님이 들어왔습니다.', 'Leave' : '님이 나갔습니다.'}
    user_dic = {}
    for t in temp: 
        if len(t)>2: 
            user_dic[t[1]] = t[2]
        if t[0] in enter_dic: 
            answer.append([t[1], enter_dic[t[0]]])
    result = [user_dic[i]+j for i, j in answer]
    return result