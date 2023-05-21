def net(n=1000000): 
    sosu=[]
    x = [False]+[True]*(n-1) 
    for i in range(2, n+1): 
        if x[i-1]:
            sosu.append(i)
            for j in range(i-1, n, i):
                x[j] = False
    return sosu

from itertools import combinations 
from itertools import permutations 
def solution(numbers):
    answer = 0
    num_list = list(numbers)
    total_nums = []
    for i in range(1, len(num_list)+1): 
        # total_nums.extend(list(combinations(numbers, i)))
        total_nums.extend(list(permutations(numbers, i)))
    total_nums = set([''.join(i).lstrip('0') for i in total_nums])
    
    result = [i for i in total_nums if i]
    sosu = net()
    
    return sum([True if (int(i) in sosu) else False for i in result])