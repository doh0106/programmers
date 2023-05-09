def solution(s):
    answer = []
    count0 = 0 
    many = 0 
    while s!='1': 
        n = len(s)
        s = s.replace('0','')
        many+=1
        c0 = n - len(s)
        count0+=c0 

        s = str(bin(len(s))[2:])
        # print(c, s)
        # break
    return [many, count0]