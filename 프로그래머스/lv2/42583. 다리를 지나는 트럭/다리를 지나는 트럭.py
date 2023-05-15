# # 내꺼 시간 초과함 
# from collections import deque 

# def solution(bl, w, truck_weights):
#     answer = 0
#     q = deque(truck_weights)
#     temp = []
#     while q: 
#         if len(temp)<bl:
#             if sum(temp) + q[0]>w: 
#                 temp.append(0)
#                 # print(temp)
#             else: 
#                 temp.append(q.popleft())
#                 # print(temp)
#         elif len(temp)==bl: 
#             temp = temp[1:]
#             if sum(temp)+q[0]<=w: 
#                 temp.append(q.popleft())
#                 # print(temp)
#             elif sum(temp)+q[0]>w: 
#                 temp.append(0)
#                 # print(temp)
#         answer += 1
#     answer += bl
#     return answer

from collections import deque

def solution(bl, w, truck_weights):
    answer = 0
    q = deque(truck_weights)
    current_weight = 0
    bridge = deque([0] * bl)
    
    while q:
        current_weight -= bridge.popleft()
        
        if current_weight + q[0] <= w:
            truck = q.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)
        
        answer += 1

    answer += bl
    return answer