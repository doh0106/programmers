from collections import deque 
def solution(prices):
    answer = []
    q = deque(prices)
    k = q.popleft()

    while q: 
        count = 0
        for i in q: 
            if i>= k:
                count +=1
            else: 
                count+=1
                break 
        answer.append(count)
        # print(k, q)
        k = q.popleft()
    answer.append(0)
    return answer