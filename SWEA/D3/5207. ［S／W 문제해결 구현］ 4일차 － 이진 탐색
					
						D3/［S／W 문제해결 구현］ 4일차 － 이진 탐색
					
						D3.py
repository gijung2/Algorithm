#이진탐색 구현

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    count = 0

    for target in B:
        left, right = 0, N - 1
        prev = 0
        while left <= right:
            mid = (left + right) // 2

            if A[mid] == target:
                count +=1
                break

            elif A[mid] <target:
                if prev == 1:
                    break

                prev = 1
                left = mid + 1

            else:
                if prev == -1:
                    break

                prev = -1
                right = mid - 1

    print(f'#{tc} {count}')


