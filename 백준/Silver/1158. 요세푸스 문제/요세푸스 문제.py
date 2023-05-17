import sys 
a, b = map(int, sys.stdin.readline().split())

from collections import deque 
q = deque(range(1, a+1))
answer = []
while q: 
    for _ in range(b-1): 
        q.append(q.popleft())
    answer.append(q.popleft())
result = ', '.join([str(i) for i in answer])
print(f'<{result}>')