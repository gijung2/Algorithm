def dfs(depth, start, path):
    if depth == M:
        print(*path)
        return

    for i in range(start, N):
        dfs(depth+1, i+1, path + [arr[i]])


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

dfs(0, 0, [])
