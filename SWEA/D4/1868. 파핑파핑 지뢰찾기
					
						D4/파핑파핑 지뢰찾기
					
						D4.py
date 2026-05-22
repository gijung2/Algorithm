from collections import deque

T = int(input())

# 8방향
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(input().strip()) for _ in range(N)]

    # visited[i][j] = 해당 칸이 이미 열린 적 있는지
    visited = [[0] * N for _ in range(N)]

    # 해당 칸 주변 8방향에 지뢰가 몇 개 있는지 세는 함수
    def count_mine(x, y):
        mine_count = 0

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == '*':
                    mine_count += 1

        return mine_count

    # 주변 지뢰가 0개인 칸을 클릭했을 때 자동으로 열리는 영역 처리
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = 1

        while q:
            cx, cy = q.popleft()

            # 현재 칸 주변에 지뢰가 있으면 더 이상 확장하지 않음
            if count_mine(cx, cy) != 0:
                continue

            # 현재 칸 주변 지뢰가 0개라면 8방향으로 확장
            for dx, dy in directions:
                nx = cx + dx
                ny = cy + dy

                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))

    click = 0

    # 1. 주변 지뢰가 0개인 칸부터 클릭
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.' and visited[i][j] == 0:
                if count_mine(i, j) == 0:
                    bfs(i, j)
                    click += 1

    # 2. 아직 안 열린 빈 칸은 각각 한 번씩 클릭
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.' and visited[i][j] == 0:
                click += 1

    print(f'#{tc} {click}')