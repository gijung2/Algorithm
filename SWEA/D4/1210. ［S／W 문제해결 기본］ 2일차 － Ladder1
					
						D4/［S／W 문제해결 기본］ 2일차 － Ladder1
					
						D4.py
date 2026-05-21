T = 10

for tc in range(1, T + 1):
    test_case = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    # 마지막 행에서 도착점 2의 위치 찾기
    x = 99
    y = arr[99].index(2)

    # 맨 위에 도착할 때까지 반복
    while x > 0:

        # 왼쪽으로 갈 수 있으면
        if y - 1 >= 0 and arr[x][y - 1] == 1:
            while y - 1 >= 0 and arr[x][y - 1] == 1:
                y -= 1
            x -= 1

        # 오른쪽으로 갈 수 있으면
        elif y + 1 < 100 and arr[x][y + 1] == 1:
            while y + 1 < 100 and arr[x][y + 1] == 1:
                y += 1
            x -= 1

        # 좌우 길이 없으면 위로 이동
        else:
            x -= 1

    print(f'#{test_case} {y}')