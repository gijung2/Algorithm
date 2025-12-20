def solution(dirs):
    answer = 0
    
    x,y =0,0
    
    visited=set()
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    dir_map = ['U', 'D', 'L', 'R']
    
    for d in dirs:
        idx = dir_map.index(d)
        nx = x + dx[idx]
        ny = y + dy[idx]
        
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
            
        path1 = (x,y,nx,ny)
        path2 = (nx, ny, x, y)
        
        if path1 not in visited:
            visited.add(path1)
            visited.add(path2)
            answer +=1
            
        x,y = nx,ny
    return answer