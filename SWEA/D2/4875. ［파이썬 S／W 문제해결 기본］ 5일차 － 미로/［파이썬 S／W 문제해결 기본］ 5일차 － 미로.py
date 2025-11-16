def search(lst, x, y, check):
    global ischeck
    dx, dy = [1,-1,0,0], [0,0,-1,1]

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < len(lst) and 0 <= yy < len(lst) and not check[xx][yy]:
            check[xx][yy] = True

            if lst[xx][yy] == 3:
                ischeck = True
            elif lst[xx][yy] == 0:
                search(lst, xx, yy, check)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    cache = [[False] * N for _ in range(N)]

    ischeck = False

    found = False
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                cache[i][j] = True
                search(maze, i, j, cache)
                found = True
                break
        if found:
            break

    print(f"#{tc} {1 if ischeck else 0}")
