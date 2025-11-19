T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    lst.sort()
    ans = "Possible"
    cnt = 0
    
    for t in lst:
        cnt += 1
        
        # t초까지 만들어진 빵 개수 = (t // M) * K
        if (t // M) * K < cnt:
            ans = "Impossible"
            break
    
    print(f"#{tc} {ans}")
