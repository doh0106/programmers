from collections import deque
def solution(s):
    q = deque(s)
    dic = {'(' : 0, ')' :0}
    while q: 
        dic[q.popleft()] += 1
        if dic[')'] > dic['(']:
            return False
    a, b = dic.values()
    if a!=b:
        return False
    return True