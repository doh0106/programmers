def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees: 
        check = 0
        temp = [i for i in skill]
        for i in s: 
            if i in temp: 
                if i!=temp[0]: 
                    check += 1
                    break 
                else: 
                    temp = temp[1:]
        if not check: 
            answer += 1
    return answer