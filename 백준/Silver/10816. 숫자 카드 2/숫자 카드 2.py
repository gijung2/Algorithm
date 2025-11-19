from collections import Counter

N = int(input())

arr1 = Counter(map(int,input().split()))

M = int(input())

arr2 = list(map(int,input().split()))

result = []

for t in arr2:
    result.append(str(arr1[t]))


print(' '.join(result))