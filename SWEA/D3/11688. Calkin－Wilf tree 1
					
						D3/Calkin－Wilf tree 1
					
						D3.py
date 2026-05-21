T = int(input())

for tc in range(1, T + 1):

    s = input().strip()

    a = 1
    b = 1

    for ch in s:
        if ch == 'L':
            b = a + b
        else:
            a = a + b

    print(f"#{tc} {a} {b}")