T = int(input())


for tc in range(1, T + 1):

    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)

    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    for i in range(N, 0, -1):

        parrent = i//2

        if parrent >= 1:

            tree[parrent] += tree[i]

    print(f'#{tc} {tree[L]}')