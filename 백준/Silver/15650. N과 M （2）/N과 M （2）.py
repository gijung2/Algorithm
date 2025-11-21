N, M = map(int,input().split())
ans = []

def dfs(n, lst):
    if n == N+1:
        if len(lst) == M:
            ans.append(lst[:])
        return

    # 선택
    dfs(n+1, lst+[n])

    # 선택 안 함
    dfs(n+1, lst)

dfs(1, [])
for lst in ans:
    print(*lst)
