N = int(input())

arr=[]

for _ in range(N):
    x,y= map(int,input().split())
    arr.append((x,y))

arr.sort()


for x, y in arr:
    print(x, y)