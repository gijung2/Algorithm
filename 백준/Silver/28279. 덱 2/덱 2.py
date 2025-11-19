import sys
from collections import deque

input = sys.stdin.readline
dq =deque()
output = []

N = int(input())

for _ in range(N):
    cmd = input().split()

    t =cmd[0]
    if t == '1':
        dq.appendleft(cmd[1])
    elif t == '2':
        dq.append(cmd[1])
    elif t == '3':
        output.append(dq.popleft() if dq else -1)
    elif t == '4':
        output.append(dq.pop() if dq else -1)
    elif t == '5':  # size
        output.append(len(dq))
    elif t == '6':  # empty
        output.append(0 if dq else 1)
    elif t == '7':  # front
        output.append(dq[0] if dq else -1)
    elif t == '8':  # back
        output.append(dq[-1] if dq else -1)

print("\n".join(map(str, output)))