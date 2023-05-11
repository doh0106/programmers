def solution(brown, yellow):
    answer = []
    num = brown+yellow
    for i in range(3, num//3+1): 
        if num%i==0:
            print(i, num//i)
            s = 2*(i+num//i-2)
            print(s)
            if s == brown: 
                answer.append([max(i, num//i), min(i, num//i)])
                break
    return answer[0]