from itertools import product
def solution(word):
    answer = 0
    a = [' ', 'A', 'E', 'I', 'O', 'U']
    temp = list(product(a, a, a, a, a))
    answer = list(set([''.join(x).strip().replace(' ', '') for x in temp]))[1:]
    answer.sort()
    return answer.index(word)+1