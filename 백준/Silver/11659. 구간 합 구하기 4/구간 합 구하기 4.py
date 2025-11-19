import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 배열 만들기
psum = [0] * (N + 1)

for i in range(1, N + 1):
    psum[i] = psum[i - 1] + arr[i - 1]

# 질의 처리
for _ in range(M):
    i, j = map(int, input().split())
    print(psum[j] - psum[i - 1])
