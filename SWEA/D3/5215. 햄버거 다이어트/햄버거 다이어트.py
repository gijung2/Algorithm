from itertools import combinations


T= int(input())

for tc in range(1, T+1):
    N,L = map(int,input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0

    for j in range(1, N+1):
        for value in combinations(data,j):
            score=0
            kcal=0

            for k in range(len(value)):
                kcal+= value[k][1]
                score+=value[k][0]

            if kcal > L:
                continue

            if max_score < score:
                max_score = score


    print(f"#{tc} {max_score}")