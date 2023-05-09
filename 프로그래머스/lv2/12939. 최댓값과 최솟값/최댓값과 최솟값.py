def solution(s):
    M = sorted(list(map(int, s.split())))[-1]
    m = sorted(list(map(int, s.split())))[0]
    
    return ' '.join([str(m), str(M)])