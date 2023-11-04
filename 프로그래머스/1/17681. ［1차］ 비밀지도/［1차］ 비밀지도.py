def num2(n, d):
    temp = ''
    while 1:
        if n < 2:
            temp += str(n)
            break
        temp += str(n%2)
        n //= 2
    if len(temp) < d:
        return '0'*(d-len(temp)) + temp[::-1]
    return temp[::-1]

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = ''
        line1 = num2(arr1[i], n)
        line2 = num2(arr2[i], n)
        # print(line1, line2)
        for x in range(n):
            if int(line1[x])+int(line2[x])!=0:
                temp += '#'
            else:
                temp += ' '
        # print(temp)
        answer.append(temp)
        
    return answer