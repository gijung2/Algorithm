N = int(input())
arr = list(map(int, input().split()))

count = 0

for k in arr:
    if k < 2:
        continue  # 1은 소수가 아님
    is_prime = True
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

print(count)
