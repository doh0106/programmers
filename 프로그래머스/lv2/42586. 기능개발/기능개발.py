from collections import deque
def solution(progresses, speeds):
    answer = []
    p = deque(progresses)
    s = deque(speeds)
    while p:
        count = 0
        for i in range(len(p)): 
            p[i]+=s[i]
        print('빼기 전',p)
        if p and p[0]>=100: 
            num = 0
            for j in range(len(p)):
                if p[j]>=100:
                    num+=1
                else:
                    break
            print(num)
            for _ in range(num):
                p.popleft()
                s.popleft()
                count+=1 
            answer.append(count)
        print('뺀 후', p)

    return answer