def solution(n, left, right):      
    temp = []
    for i in range(left, right+1): 
        row = i//n
        col = i%n
        if row==col: 
            temp.append((row+col)//2+1)
        elif row>col: 
            temp.append(row+1)
        elif row<col: 
            temp.append(col+1)
    return temp