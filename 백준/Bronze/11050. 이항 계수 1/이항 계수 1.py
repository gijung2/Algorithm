from itertools import combinations

N,K = map(int,input().split())

cnt = 0
for _ in combinations(range(N),K):
    cnt +=1

print(cnt)