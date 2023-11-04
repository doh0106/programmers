def solution(s):
    answer = []
    alpha_dic = {}
    for idx, alpha in enumerate(s):
        if alpha not in alpha_dic:
            alpha_dic[alpha]=idx
            answer.append(-1)
        else:
            answer.append(idx-alpha_dic[alpha])
            alpha_dic[alpha]=idx
    return answer