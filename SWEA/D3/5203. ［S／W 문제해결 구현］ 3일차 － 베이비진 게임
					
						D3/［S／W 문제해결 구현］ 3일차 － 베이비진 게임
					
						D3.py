T = int(input())

for tc in range(1, T + 1):

    arr = list(map(int, input().split()))

    p1 = [0] * 10
    p2 = [0] * 10

    answer = 0

    def check(player):

        # triplet 검사
        for i in range(10):
            if player[i] >= 3:
                return True

        # run 검사
        for i in range(8):
            if player[i] >= 1 and player[i + 1] >= 1 and player[i + 2] >= 1:
                return True

        return False
    
    for i in range(12):   # 여기 수정
        if i % 2 == 0:
            p1[arr[i]] += 1

            if check(p1):
                answer = 1
                break
        else:
            p2[arr[i]] += 1

            if check(p2):
                answer = 2
                break

    print(f'#{tc} {answer}')