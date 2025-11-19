N, M = map(int, input().split())

def permu(arr, n, m):
    if len(arr) == m:                # 원하는 길이 수열 완성되면 출력
        print(*arr)                  # 리스트 언패킹해서 출력 형식 맞춤
        return

    for num in range(1, n + 1):      # 1 ~ N 숫자들 중에서
        if num not in arr:           # 중복 방지
            arr.append(num)          # 선택
            permu(arr, n, m)         # 다음 깊이로 탐색
            arr.pop()                # 백트래킹 (원상 복구)

# 함수는 딱 한 번만 호출해야 함
permu([], N, M)
