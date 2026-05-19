T = int(input())


def isplus(ar):

    s2 = str(ar)
    for i in range(len(s2)-1):
        if s2[i] > s2[i+1]:
            return False
        
    return True


for tc in range(1, T + 1):

    N = int (input())

    arr = list(map(int, input().split()))
    maximum = -1
    for i in range(N-1):
        for j in range(i+1, N):

            ar = arr[i] * arr[j]

            if isplus(ar):

                maximum = max(maximum, ar)


    print(f'#{tc} {maximum}')

