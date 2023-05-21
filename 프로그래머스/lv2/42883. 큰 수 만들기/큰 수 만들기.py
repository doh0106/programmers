# 맞는데 시간초과
# def solution(number, k):
#     answer = ''
#     count = 0 
#     l = len(number)
#     num = list(number)
#     while count < k: 
#         for i in range(l-1): 
#             if num[i]<num[i+1]: 
#                 num.pop(i)
#                 count+=1
#                 l-=1
#                 break
#     return ''.join(num)


# chat gpt 
def solution(number, k):
    stack = []
    for digit in number:
        while stack and stack[-1] < digit and k > 0:
            stack.pop()
            k -= 1
        stack.append(digit)

    # 남은 k가 0보다 큰 경우, 뒤에서부터 k개의 숫자를 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)
