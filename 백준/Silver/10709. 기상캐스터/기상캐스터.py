def solove():
    H, W = map(int,input().split())

    clouds = [input().rstrip() for _ in range(H)]
    result = [[-1] * W for _ in range(H)]

    for r in range(H):# 한줄씩 가져오기
        last_cloud = -1
        for current_pos in range(W): #한 칸씩 이동하기
            #만약 지금 칸이 구름('c') 이라면?
            if clouds[r][current_pos] == 'c':
                last_cloud = current_pos
                result[r][current_pos] = 0
            #만약 지금 칸이 구름이 아니라면?
            else:
                if last_cloud == -1: #구름이 한번도 나온적이 없다면?
                    result[r][current_pos] = -1
                else:
                    result[r][current_pos] = current_pos - last_cloud

    for row in result:
        print(*row)

solove(  )