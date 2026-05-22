T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input().split()))

    def quick_sort(arr):
        # 원소가 1개 이하이면 이미 정렬된 상태
        if len(arr) <= 1:
            return arr

        # 기준값 pivot
        pivot = arr[0]

        left = []
        right = []

        # pivot을 제외한 나머지 원소 분류
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])

        # 왼쪽 정렬 + pivot + 오른쪽 정렬
        return quick_sort(left) + [pivot] + quick_sort(right)

    sorted_arr = quick_sort(arr)

    print(f'#{tc} {sorted_arr[N // 2]}')