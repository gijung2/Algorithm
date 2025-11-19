import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque(range(1, N+1))

while len(q) > 1:
    q.popleft()           # 1. 맨 위 버리기
    q.append(q.popleft()) # 2. 다음 맨 위를 아래로 이동

print(q[0])
