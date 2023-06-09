def solution(n, s):
    if n>s: 
        return [-1]
    answer = []
    a = s//n 
    print(a)
    for _ in range(n):
        answer.append(a)
    idx = 0
    x = sum(answer)
    while x!=s: 
        answer[idx]+=1
        idx += 1
        x+=1
    return sorted(answer)