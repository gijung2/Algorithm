T = int(input().strip())
primes = [2, 3, 5, 7, 11]

for tc in range(1, T + 1):
    n = int(input().strip())
    exps = []

    for p in primes:
        cnt = 0
        while n % p == 0:
            n //= p
            cnt += 1
        exps.append(cnt)

    # 형식: #테스트번호 a b c d e
    print(f"#{tc} {' '.join(map(str, exps))}")
