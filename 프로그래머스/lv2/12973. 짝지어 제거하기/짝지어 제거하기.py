from collections import deque
def solution(s):
    q = deque(s) 
    answer = []
    while q: 
        answer.append(q.popleft())
        if len(answer)>=2:
            if answer[-1]==answer[-2]:
                answer.pop()
                answer.pop()
    if answer: 
        return 0
    else: 
        return 1
