T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())

    pizza =list(map(int,input().split()))
    cheese = []

    for i in range(M):
        cheese.append([i+1, pizza[i]])
    oven = cheese[:N]
    remain = cheese[N:]

    while len(oven) > 1:
        check = oven.pop(0)
        check[1] //=2

        if check[1] ==0:
            if remain:
                oven.append(remain.pop(0))
        else:
            oven.append(check)

    print(f"#{tc} {oven[0][0]}")