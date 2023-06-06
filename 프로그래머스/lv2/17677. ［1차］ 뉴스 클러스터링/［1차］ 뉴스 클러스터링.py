def solution(str1, str2):
    answer = 0
    l1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    l2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    s1 = list(set(l1))
    s2 = list(set(l2))
    dic1 = dict(zip(s1,[l1.count(i) for i in s1]))
    dic2 = dict(zip(s2,[l2.count(i) for i in s2]))
    uni_key = [i for i in dic1.keys() if i in dic2.keys()]
    m = 0 
    M = 0 
    print(uni_key)
    for u in uni_key: 
        m+=min(dic1[u], dic2[u])
    M = len(l1)+len(l2)-m
    if M:
        result = int(m/M*65536)
    else: 
        result = 65536
    return result