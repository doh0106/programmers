from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse = True))
    
    while len(people) > 1:
        if people[0] + people[-1] <= limit: # 최댓값과 최솟값 묶어서 보트태움
            answer += 1
            people.pop()    #최소 빼내고
            people.popleft()    #최대 빼내고
        else:
            answer += 1
            people.popleft()
            
    if people:  #people에 1명 남아있는 경우 처리
        answer += 1
                
    return answer

"""
이진 탐색 사용: 현재 구현에서는 tp 리스트에서 최솟값을 찾기 위해 선형 탐색을 수행하고 있습니다. 이를 이진 탐색으로 변경하면 탐색 시간을 줄일 수 있습니다. bisect_left 함수를 사용하여 이진 탐색을 구현할 수 있습니다.

인덱스 사용: 현재 구현에서는 people 리스트에서 원소를 제거하는 과정에서 리스트를 조작하고 있습니다. 리스트 조작은 O(n)의 시간 복잡도를 가지므로, 인덱스를 활용하여 해당 원소를 제거하는 방식으로 변경하면 시간을 절약할 수 있습니다.

반복문 줄이기: 현재 구현에서는 people 리스트가 빈 리스트가 될 때까지 반복문을 수행하고 있습니다. 하지만 탐색 범위를 조절하여 반복문을 줄일 수 있습니다. 예를 들어, 현재 남은 사람들 중에서 최소 무게의 사람과 최대 무게의 사람의 합이 limit을 초과하는 경우에는 최대 무게의 사람만 구명보트를 사용하면 됩니다.
"""