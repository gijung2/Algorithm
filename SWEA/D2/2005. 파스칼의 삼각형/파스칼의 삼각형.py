T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * (N+1) for _ in range(N+1)]

    arr[1][1] = 1   # 첫 줄

    for i in range(2, N+1):
        for j in range(1, i+1):
            if j == 1 or j == i:   # 양 끝은 1
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{tc}')
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(arr[i][j], end=' ')
        print()
