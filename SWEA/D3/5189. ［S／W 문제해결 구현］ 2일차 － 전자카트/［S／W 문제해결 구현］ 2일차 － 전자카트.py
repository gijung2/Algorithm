T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    visited[0] = 1

    answer =[10**9]

    def dfs(now, cnt, total):

        if total >= answer[0]:
            return
        
        if cnt == N:

            answer[0] = min(answer[0], total + arr[now][0])
            return

        for next_pos in range(1, N):

            if visited[next_pos] ==0:
                visited[next_pos] = 1
                dfs(next_pos, cnt +1 , total + arr[now][next_pos])
                visited[next_pos] = 0

    dfs(0, 1, 0)

    print(f'#{tc} {answer[0]}')