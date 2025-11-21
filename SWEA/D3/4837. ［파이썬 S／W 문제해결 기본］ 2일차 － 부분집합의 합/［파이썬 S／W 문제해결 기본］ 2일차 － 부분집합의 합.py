def dfs(idx, cnt, total):
    global ans, N, K, lst

    # 부분집합 길이 초과 시 중단
    if cnt > N:
        return

    # 모든 원소 확인한 경우
    if idx == 12:
        if cnt == N and total == K:
            ans += 1
        return

    # 현재 숫자를 선택하는 경우
    dfs(idx + 1, cnt + 1, total + lst[idx])

    # 현재 숫자를 선택하지 않는 경우
    dfs(idx + 1, cnt, total)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    lst = list(range(1, 13))  # 4837 문제는 숫자가 1~12 고정
    ans = 0

    dfs(0, 0, 0)

    print(f"#{tc} {ans}")
