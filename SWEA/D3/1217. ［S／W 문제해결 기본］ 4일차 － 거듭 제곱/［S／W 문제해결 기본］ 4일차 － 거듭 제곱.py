def power(n, m):
    if m == 0:
        return 1
    return n * power(n, m-1)


for _ in range(10):          
    tc = int(input())
    N, M = map(int, input().split())
    print(f"#{tc} {power(N, M)}")
