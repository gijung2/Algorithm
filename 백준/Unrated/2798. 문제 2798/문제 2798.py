from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

for comb in combinations(arr, 3):
    s = sum(comb)
    if s <= M:
        answer = max(answer, s)

print(answer)
