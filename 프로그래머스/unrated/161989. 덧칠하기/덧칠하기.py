def solution(n, m, section):
    answer = 0
    wall = [True]*n 
    for s in section: 
        wall[s-1]=False 
    for idx in range(len(wall)): 
        if not wall[idx]: 
            wall[idx:idx+m]=[True]*m
            answer+=1
    return answer