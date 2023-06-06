def jinsoo(n, x): 
    temp = []
    j_dic = dict(zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']))
    while x>=n: 
        temp.append(x%n)
        x = x//n
    temp.append(x)
    return ''.join([j_dic[i] for i in temp[::-1]])

def solution(n, t, m, p):
    answer = ''
    i = 0
    while len(answer)<t*m: 
        answer += jinsoo(n, i)
        i += 1
    return answer[p-1::m][:t]