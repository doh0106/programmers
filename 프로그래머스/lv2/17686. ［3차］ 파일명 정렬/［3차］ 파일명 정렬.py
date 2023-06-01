def solution(files):
    temp = []
    for order, f in enumerate(files):
        f_ori = f
        head, number = '', ''
        n = len(f)
        idx = 0
        for i in f: 
            if not i.isnumeric(): 
                head+=i 
            else: 
                break
        f = f.strip(head)
        for i in f: 
            if i.isnumeric(): 
                number += i
                if len(number)==5: 
                    break 
            else: 
                break 
        head = head.lower()
        number = f'{int(number):05d}'
        temp.append((f_ori, head, number, order))
    temp.sort(key=lambda x:(x[1], x[2], x[3]))
    return [i[0] for i in temp]