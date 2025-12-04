def solution(elements):
    n  = len(elements)
    arr = elements
    arr2 = arr*2
    
    result = set()
    for length in range(1,n+1):
        for start in range(n):
            sub = arr2[start:start+length]
            
            total = sum(sub)
            result.add(total)
            
    return len(result)