M = int(input())
N = int(input())

primes = []

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True

for i in range(M, N + 1):
    if is_prime(i):
        primes.append(i)

if not primes:  # 소수가 하나도 없으면
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
