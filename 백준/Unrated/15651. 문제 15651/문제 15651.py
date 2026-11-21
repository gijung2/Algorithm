N,M = map(int,input().split())
ans = []
v = [0] *(N+1)

def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    for j in range(1,N+1):
        dfs(n+1, lst+[j])

dfs(0, [])
for lst in ans:
    print(*lst)