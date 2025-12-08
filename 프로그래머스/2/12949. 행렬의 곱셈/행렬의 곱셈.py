def solution(arr1, arr2):
    answer = []
    m, n, r = len(arr1), len(arr1[0]), len(arr2[0])
    
    for i in range(m):
        arr = arr1[i]
        result = []
        for j in range(r):
            gop = 0
            for k in range(n):
                gop += arr[k] * arr2[k][j]
            result.append(gop)
        answer.append(result)
    return answer