def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    day_dic = dict(zip(months, days))
    ans_dic = dict(zip([1, 2, 3, 4, 5, 6, 0],['FRI','SAT', 'SUN','MON','TUE','WED','THU']))
    count = 0
    if a>1:
        for i in range(1, a): 
            count += day_dic[i]
    count += b
    count %= 7
    answer = ans_dic[int(count)]
    return answer