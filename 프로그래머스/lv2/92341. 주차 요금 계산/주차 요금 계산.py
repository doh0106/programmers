def solution(fees, records):
    answer = []
    d = {}
    for r in records: 
        a, b, c = r.split() 
        t = int(a.split(':')[0])*60+int(a.split(':')[1])
        if b not in d: 
            d[b]=[t]
        else: 
            d[b].append(t) 
    temp = [] 
    for k in sorted(d.keys()):
        if len(d[k])%2==0:
            temp.append(d[k])
        else: 
            temp.append(d[k]+[23*60+59]) 
    for t in temp: 
        l1 = sum(t[::2])
        l2 = sum(t[1::2])
        k = l2-l1 
        if (k-fees[0])/fees[2] == int((k-fees[0])/fees[2]):
            p = (k-fees[0])//fees[2]
        else: 
            p = (k-fees[0])//fees[2]+1
        if p>0:
            answer.append(fees[1]+p*fees[3])
        else: 
            answer.append(fees[1])
    return answer