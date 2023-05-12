from itertools import permutations

def solution(k, dungeons):
    answer = []
    a = list(permutations(dungeons,len(dungeons)))
    
    for i in a: 
        count=0
        pirodo = k
        for m, use in i: 
            if pirodo>=m: 
                pirodo-=use
                count +=1
            else: 
                break
        answer.append(count)
    return max(answer)