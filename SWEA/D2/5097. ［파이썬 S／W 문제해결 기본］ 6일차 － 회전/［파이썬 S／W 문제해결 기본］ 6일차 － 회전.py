
T = int(input().strip())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = arr[M%N]
    print(f"#{tc} {ans}")