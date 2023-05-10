from collections import deque
def solution(n, words):
    spoken = []
    q = deque(words)
    count = 1
    spoken.append(q.popleft())
    while q: 
        temp = q.popleft() 
        if temp not in spoken and spoken[-1][-1]==temp[0]: 
            spoken.append(temp)
            count += 1
        else: 
            break 
    if count == len(words): 
        return [0, 0]
    return [count%n+1, (count)//n+1]