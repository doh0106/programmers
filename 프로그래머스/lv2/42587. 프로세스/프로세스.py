from collections import deque 
def solution(priorities, location):
    p = deque(sorted(priorities, reverse=True))
    q = deque([(idx, p) for idx, p in enumerate(priorities)])
    count = 0
    while q: 
        k = q.popleft() 
        if k[-1]<p[0]:
            q.append(k)
        else:
            p.popleft()
            count+=1
            if k[0]==location:
                break
    return count