import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 1. 정렬 + 중복 제거
sorted_unique = sorted(set(arr))

# 2. 각 값 → 압축된 인덱스로 매핑
compressed = {value: index for index, value in enumerate(sorted_unique)}

# 3. 원래 순서대로 매핑값 출력
print(' '.join(str(compressed[x]) for x in arr))
