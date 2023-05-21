def solution(n, left, right):
    result = []
    for idx in range(left, right+1): 
        new_col = idx%n 
        new_row = idx//n
        if new_row>=new_col: 
            result.append(new_row+1)
        else: 
            if not result:
                result.append(new_col+1)
            else:
                result.append(result[-1]+1)
    return result