## 기존 내 꺼 : 시간 초과
# from itertools import product, combinations
# def solution(clothes):
#     answer = 0
#     c_dic = {}
#     for c, t in clothes: 
#         if t not in c_dic:
#             c_dic[t] = [c]
#         else: 
#             c_dic[t].append(c)
            
#     aw = []
#     for i in range(1, len(c_dic.keys())+1):
#         aw.extend(list(combinations(c_dic.keys(), i)))

#     for i in aw: 
#         count = len(list(product(*[c_dic[j] for j in i])))
#         answer += count
#     return answer
"""의상 종류별로 개수를 세지 않고 직접 계산: 현재 코드에서는 의상 종류(t)별로 개수를 세고 있습니다. 하지만 이 정보를 직접 세는 대신, 의상 종류의 개수를 카운트하는 대신에 모든 의상을 입지 않은 상태(None)도 포함하여 계산할 수 있습니다. 이렇게 하면 각 의상 종류별 개수를 세지 않고도 조합의 수를 계산할 수 있습니다.

조합 계산에서 product 함수를 사용하지 않고 바로 계산: 현재 코드에서는 product 함수를 사용하여 의상 종류별로 가능한 조합을 계산한 후, 각 조합에 대해 len 함수를 호출하여 개수를 계산합니다. 하지만 product 함수를 사용하지 않고 바로 조합의 수를 계산할 수 있습니다. 의상 종류별로 개수를 저장하지 않고, 해당 종류의 의상을 입을지 입지 않을지를 2로 나타내는 이진 숫자로 표현한 후, 가능한 모든 이진 숫자의 조합의 수를 계산합니다.

불필요한 변수와 반복문 제거: 현재 코드에서 aw라는 변수를 사용하여 가능한 모든 조합을 저장하고 있습니다. 하지만 이 변수를 사용하지 않고도 바로 계산할 수 있습니다. 또한, 중간 단계에서 사용하는 count 변수도 제거할 수 있습니다."""
# chat gpt 
def solution(clothes):
    answer = 1
    c_dic = {}
    
    for c, t in clothes:
        if t not in c_dic:
            c_dic[t] = 1
        else:
            c_dic[t] += 1
    
    for count in c_dic.values():
        answer *= (count + 1)  # 각 의상 종류별 개수에 1을 더해서 곱해줌
    
    return answer - 1  # 아무것도 입지 않은 경우는 제외해야 하므로 1을 빼줌