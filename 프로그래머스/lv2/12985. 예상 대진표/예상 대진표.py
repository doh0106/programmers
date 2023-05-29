def solution(n, x, y):
    answer = 1
    a, b = min(x, y), max(x, y)
    while True:
        if b == a+1 and b % 2 == 0:
            break
        if a != 1:
            a = (a+1)//2
        b = (b+1)//2
        answer += 1

    return answer