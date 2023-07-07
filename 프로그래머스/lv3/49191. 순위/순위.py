def solution(n, results):
    answer = 0
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for a, b in results: 
        a-=1
        b-=1
        graph[a][b]=1
        graph[b][a]=-1
    for way in range(n): 
        for start in range(n): 
            for end in range(n): 
                if start==way or start==end or way==end: 
                    continue 
                if graph[start][way]==graph[way][end]==1:
                    graph[start][end]=1
                elif graph[start][way]==graph[way][end]==-1:
                    graph[start][end]=-1
    for g in graph: 
        if g.count(0)==1:
            answer+=1
    return answer