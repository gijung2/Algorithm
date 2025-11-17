for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))


    result =0
    for i in range(2, N-2):
        around = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])

        if arr[i] > around:
            result += arr[i] - around

    print(f"#{tc} {result}")



