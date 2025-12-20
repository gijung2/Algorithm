def solution(d, budget):
    d.sort()
    total = 0
    cnt = 0
    
    for x in d:
        if total + x > budget:
            break
            
        total += x
        cnt+=1
    return cnt