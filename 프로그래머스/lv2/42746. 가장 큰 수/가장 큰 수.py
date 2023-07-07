def solution(numbers):
    answer = ''
    temp = []
    for n in numbers:
        temp.append(str(n))
    temp.sort(key=lambda x: (x*3, -len(x)), reverse=True)
    result = ''.join(temp)
    if result.lstrip('0'): 
        return result
    return '0'

