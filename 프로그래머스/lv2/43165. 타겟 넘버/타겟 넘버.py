temp = []
def my_sol(numbers, total, idx): 
    if idx == len(numbers): 
        temp.append(total)
        return 
    plus  = total+numbers[idx]
    minus = total-numbers[idx]
    idx+=1
    return my_sol(numbers, plus, idx), my_sol(numbers,  minus, idx)
        
def solution(numbers, target):   
    my_sol(numbers, 0, 0)
    return temp.count(target)