from collections import deque
def solution(s):
    answer = []
    temp = ''
    q = s[1:-1]
    for i in q:
        # print(i)
        if i =='{':
            check=1
            continue
        elif i=='}':
            answer.append([int(j) for j in temp.split(',')])
            temp=''
            check=0
        if check ==1:
            temp+=i
            continue
    answer.sort(key=lambda x:len(x))
    result = []
    for a in answer: 
        for x in a: 
            if x not in result:
                result.append(x)
    return result