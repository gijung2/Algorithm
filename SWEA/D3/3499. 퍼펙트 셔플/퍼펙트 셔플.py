T = int(input())

for tc in range(T):
    N = int(input())
    N_lst = input().split()

    # 카드 분할
    if N % 2 == 0:
        left = N_lst[:N//2]
        right = N_lst[N//2:]
    else:
        left = N_lst[:(N//2)+1]
        right = N_lst[(N//2)+1:]

    # right를 left 사이사이에 삽입
    idx = 1
    for card in right:
        left.insert(idx, card)
        idx += 2

    print(f"#{tc+1} {' '.join(left)}")
