def solution(want, number, discount):
    answer = 0
    j_dic = dict(zip(want, number))
    for i in range(len(discount)-sum(number)+1): 
        temp_dic = {}
        for j in discount[i:i+sum(number)]: 
            if j not in temp_dic: 
                temp_dic[j] = 1
            else: 
                temp_dic[j] += 1
        if temp_dic == j_dic: 
            # print(temp_dic)
            answer += 1
    return answer