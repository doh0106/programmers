def make_3num(n): 
    temp = []
    while n >=3: 
        temp.append(n%3)
        n = n//3
    temp.append(n)
    return ''.join(str(i) for i in temp)

def solution(n):
    a = make_3num(n).lstrip('0')
    return int(a, 3)
