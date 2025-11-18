N, M = map(int, input().split())

board = [input().strip() for _ in range(N)]
result = []

for i in range(N - 7):
    for j in range(M - 7):

        draw1 = 0
        draw2 = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):  

                if (a + b) % 2 == 0:    # 짝수 칸 = 시작 색과 동일해야 하는 칸

                    if board[a][b] != 'B':    # 시작이 B라고 가정했는데 현재 B 아니면 칠하기
                        draw1 += 1
                    if board[a][b] != 'W':    # 시작이 W라고 가정했는데 현재 W 아니면 칠하기
                        draw2 += 1

                else:                          # 홀수 칸 = 반대 색이어야 하는 칸

                    if board[a][b] != 'W':    # B-start면 홀수칸은 W여야 함
                        draw1 += 1
                    if board[a][b] != 'B':    # W-start면 홀수칸은 B여야 함
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))
