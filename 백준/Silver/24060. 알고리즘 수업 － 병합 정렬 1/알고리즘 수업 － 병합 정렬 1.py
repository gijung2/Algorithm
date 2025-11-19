def merge_sort(A, p, r, K):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q, K)
        merge_sort(A, q + 1, r, K)
        merge(A, p, q, r, K)


def merge(A, p, q, r, K):
    global cnt, result
    
    tmp = []
    i, j = p, q + 1

    # 두 배열 병합
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    # 남은 왼쪽
    while i <= q:
        tmp.append(A[i])
        i += 1

    # 남은 오른쪽
    while j <= r:
        tmp.append(A[j])
        j += 1

    # tmp -> A에 복사 + 저장 횟수 카운트
    t = 0
    for idx in range(p, r + 1):   # k 쓰면 안 됨!
        A[idx] = tmp[t]
        t += 1
        cnt += 1
        
        if cnt == K:
            result = A[idx]


# 입력
N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
result = -1

merge_sort(A, 0, N - 1, K)

print(result)
