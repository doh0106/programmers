def solution(s):
    eng2num = dict(zip(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 
                       'eight', 'nine'], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    for i in eng2num:
        s = s.replace(i, str(eng2num[i]))
    return int(s)