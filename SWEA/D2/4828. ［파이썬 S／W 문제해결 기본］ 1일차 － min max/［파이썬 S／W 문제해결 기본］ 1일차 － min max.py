T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    max_val = -float('inf')
    min_val = float('inf')

    # 최댓값 찾기
    for x in nums:
        if x > max_val:
            max_val = x

    # 최솟값 찾기
    for x in nums:
        if x < min_val:
            min_val = x

    print(f"#{tc} {max_val - min_val}")
