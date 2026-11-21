N, M = map(int, input().split())


arr1= set()
arr2=[]
for nc in range(N):
    arr1.add(input())

for mc in range(M):
    arr2.append(input())

cnt = 0

for x in arr2:
    if x in arr1:
        cnt +=1

print(cnt)