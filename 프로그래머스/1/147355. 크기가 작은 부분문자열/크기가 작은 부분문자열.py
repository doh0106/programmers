def solution(t, p):
    answer = 0
    n = len(p)
    for i in range(len(t)-n+1):
        answer += int(t[i:i+n]<=p)
    return answer