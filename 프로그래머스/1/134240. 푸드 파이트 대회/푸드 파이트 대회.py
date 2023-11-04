def solution(food):
    answer = ''
    for idx, f in enumerate(food[1:]):
        # print(f//2, str(idx+1))
        num = f//2
        answer += str(idx+1)*num
    return answer + '0' + answer[::-1]