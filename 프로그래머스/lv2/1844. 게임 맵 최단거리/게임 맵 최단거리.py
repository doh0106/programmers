from collections import deque 
temp = []

def solution(maps):
    w = len(maps[0])
    h = len(maps)
    temp = [] 
    q = deque()
    start = (0, 0, 0)
    q.append(start)
    visited = [[False]*w for _ in range(h)]
    visited[0][0]=True
    distances = [[0]*w for _ in range(h)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q: 
        x, y, total = q.popleft()
        if x == w-1 and y==h-1: 
            temp.append(total)
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<w and 0<=ny<h and not visited[ny][nx] and maps[ny][nx]==1: 
                q.append((nx, ny, total+1))
                distances[ny][nx]=total+1
                visited[ny][nx]=True
                # print(np.array(distances), q, '\n')
    if temp: 
        return sorted(temp)[0]+1
    else: 
        return -1
