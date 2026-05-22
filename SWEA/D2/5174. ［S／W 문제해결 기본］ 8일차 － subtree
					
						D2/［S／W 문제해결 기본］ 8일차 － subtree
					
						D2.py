T = int(input())

def preord(n):
    if n:
        global ans
        ans += 1
        preord(ch1[n])
        preord(ch2[n])

for tc in range(1, T + 1):

    E, S = map(int, input().split())
    lst = list(map(int, input().split()))

    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)

    for i in range(0, len(lst), 2):
        p, c = lst[i], lst[i + 1]

        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    ans = 0

    preord(S)

    print(f'#{tc} {ans}')