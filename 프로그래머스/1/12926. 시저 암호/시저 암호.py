def solution(s, n):
    answer = ''
    # print('a-z')
    large='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small= 'abcdefghijklmnopqrstuvwxyz'
    temp = ''
    # print(small[0])
    for i in s:
        if i == ' ':
            answer += ' '
        elif i.isupper():
            answer += large[(large.index(i)+n)%26]
        elif i.islower():
            answer += small[(small.index(i)+n)%26]
    return answer