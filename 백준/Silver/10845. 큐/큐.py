import sys 

n = int(sys.stdin.readline().rstrip())

que = []
for i in range(n): 
    order = sys.stdin.readline().rstrip() 
    if order.startswith('push'): 
        o1, o2 = order.split()
        que.append(int(o2))
    elif order == 'pop': 
            if que: 
                print(que[0])
                que = que[1:]
            else: 
                print(-1)
    elif order == 'size': 
        print(len(que))
    elif order == 'empty': 
        if que: 
            print(0)
        else: 
            print(1)
    elif order == 'front': 
        if que: 
            print(que[0])
        else: 
            print(-1)
    elif order == 'back': 
        if que: 
            print(que[-1])
        else: 
            print(-1)