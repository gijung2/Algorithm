def dfs(i,j):
    stack = [(i,j)]
    a[i][j] = 0
    area =1
    while stack:
        x,y = stack.pop()
        
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx,y+dy
            
            if 0<=nx<n and 0<= ny <m and a[nx][ny]==1:
                a[nx][ny]=0
                stack.append((nx,ny))
                area +=1
    
    return area

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
count =0
max_area = 0

for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            count += 1
            max_area = max(max_area, dfs(i,j))
            
print(count)
print(max_area)