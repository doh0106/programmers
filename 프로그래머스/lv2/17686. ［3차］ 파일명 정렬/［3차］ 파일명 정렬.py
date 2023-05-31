def solution(files):
    answer = []
    for i, f in enumerate(files): 
        head = '' 
        number = ''
        for x in f: 
            if not x.isnumeric(): 
                head+=x
            else: 
                break 
        temp_f = f.lstrip(head)
        head = head.lower()
        for x in temp_f: 
            if x.isnumeric(): 
                number += x 
            else: 
                break 
        number = f'{int(number):05d}'        
        print(f, head, number)
        
        # idx = 0 
        # n_idx = 0
        # while not f[idx].isnumeric(): 
        #     idx += 1
        #     n_idx += 1
        # head = f[:idx].lower()
        # while f[n_idx].isnumeric(): 
        #     n_idx += 1
        # number = f'{int(f[idx:n_idx]):05d}'
        temp = [f, head, number, i]
        answer.append(temp)
    answer.sort(key=lambda x:(x[1], x[2], x[3]))
    return [x[0] for x in answer]