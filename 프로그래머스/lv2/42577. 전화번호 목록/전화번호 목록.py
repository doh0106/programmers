## 기존 꺼 : 답은 맞는데 시간 초과 

# def solution(phone):
#     answer = True
#     for i in range(len(phone)-1):
#         for j in range(i+1, len(phone)):
#             # print(i, j)
#             a, b = sorted([phone[i], phone[j]],key=lambda x:len(x))
#             print(a, b)
#             if not b.startswith(a): 
#                 continue
#             else: 
#                 return False
#     return answer

# chat gpt 풀이

def solution(phone):
    phone.sort(key=lambda x: len(x))
    answer = True
    hash_set = set()
    for number in phone:
        for i in range(1, len(number)):
            prefix = number[:i]
            if prefix in hash_set:
                return False
        hash_set.add(number)
    return answer
