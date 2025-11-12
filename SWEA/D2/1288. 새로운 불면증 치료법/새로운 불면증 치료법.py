T = int(input().strip())

for i in range(1, T + 1):
    N = int(input().strip())
    seen = set()
    k = 0

    while len(seen) < 10:
        k += 1
        num = k * N
        for j in str(num):   
            seen.add(j)

    print(f"#{i} {num}")
