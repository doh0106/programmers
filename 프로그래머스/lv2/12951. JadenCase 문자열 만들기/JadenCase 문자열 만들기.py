from collections import deque
def solution(string):
    answer = ''
    s = deque(string)
    while s: 
        k = s.popleft()
        if not answer: 
            answer+=k.upper()
        else:
            if answer[-1]==' ':
                answer+=k.upper()
            else:
                answer+=k.lower()
                
    return answer