def solution(n):
    answer = [[0]*n for _ in range(n)]
    l = []
    dic = {0:[0,1], 1:[1,0],2:[0,-1], 3:[-1, 0]}
    for idx in range(1, 2*n): 
        if idx%2 ==0:
            l.append(n-idx//2)
        else: 
            l.append(n-idx//2)
    l[0]-=1
    start = [0, 0]
    count = 1
    answer[0][0]=count
    for idx, k in enumerate(l): 
        direction = idx%4
        for _ in range(k): 
            count+=1
            start = [x+y for x,y in zip(start,dic[direction])]
            a, b = start
            answer[a][b]=count
    return answer