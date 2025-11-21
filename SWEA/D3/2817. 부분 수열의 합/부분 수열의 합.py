T = int(input())

def dfs(idx, s):
    global cnt
    if s > K:
        return
    if idx == N:
        if s == K:
            cnt += 1
        return

    dfs(idx + 1, s + arr[idx])  # 선택
    dfs(idx + 1, s)             # 비선택


for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    dfs(0, 0)
    print(f"#{tc} {cnt}")
