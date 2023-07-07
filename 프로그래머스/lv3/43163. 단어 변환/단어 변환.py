from collections import deque 

def compare(a, b): 
    count = 0
    for i, j in zip(a, b): 
        if i!=j: 
            count+=1
    if count == 1:
        return True
    else: 
        return False

def solution(begin, target, words):
    if target not in words: 
        return 0

    words = [begin]+words
    n = len(words)
    temp = [[] for _ in range(n)]

    for i in range(n): 
        for j in range(n): 
            if compare(words[i], words[j]):
                if j not in temp[i]:
                    temp[i].append(j)
                    
    end = words.index(target)
    q = deque() 
    q.append((0, 0))
    answer = []

    visited = set()
    visited.add(0)
    
    while q: 
        node, total = q.popleft() 
        if node == end: 
            answer.append(total)
        for next_node in temp[node]: 
            if next_node not in visited:
                visited.add(next_node)
                q.append((next_node, total+1))
    if answer:
        return sorted(answer)[0]
    else: 
        return 0
