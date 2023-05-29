def solution(msg):
    answer = []
    d = dict(zip([chr(i+65) for i in range(26)], list(range(1,27))))
    while msg:
        idx = 0 
        for _ in range(len(msg)):
            if msg[:idx+1] in d: 
                idx += 1 
            else: 
                d[msg[:idx+1]] = len(d)+1
                break
        answer.append(d[msg[:idx]])
        msg = msg[idx:]
    return answer