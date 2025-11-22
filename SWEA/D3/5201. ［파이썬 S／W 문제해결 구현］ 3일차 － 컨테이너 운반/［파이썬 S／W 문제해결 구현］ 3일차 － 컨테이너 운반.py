T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))  # 컨테이너 무게
    Tlist = list(map(int, input().split()))  # 트럭 용량

    
    W.sort(reverse=True)
    Tlist.sort(reverse=True)
    ans = 0
    idx = 0
    for t in Tlist:
        while idx <N:
            if W[idx] <= t:
                ans += W[idx]
                idx+=1
                break
            idx+=1


    print(f"#{tc} {ans}")