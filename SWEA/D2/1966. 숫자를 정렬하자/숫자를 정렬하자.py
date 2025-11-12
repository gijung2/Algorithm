T = int(input().strip())

for tc in range(1, T+1):

    N = int(input().strip())

    nums =list(map(int, input().strip().split(' ')))

    nums.sort()
    print(f"#{tc} {' '.join(map(str, nums))}")