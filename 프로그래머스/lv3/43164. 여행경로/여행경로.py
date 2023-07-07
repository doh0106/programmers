from collections import defaultdict, deque 
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for s, e in tickets: 
        graph[s].append(e)
        
    paths = []
    visited = set() 
    
    q = deque()    
    q.append(('ICN', [], tickets))
    
    while q: 
        node, path, left= q.popleft() 
        if not left: 
            paths.append(path+[node])
        for next_node in graph[node]: 
            if [node, next_node] in left: 
                left_copy = left.copy()
                left_copy.remove([node, next_node])
                q.append((next_node, path+[node], left_copy))
    paths.sort()
    return paths[0]