from collections import Counter

def solution(k, tangerine):
    arr = Counter(tangerine)
    
    new_arr = sorted(arr.items(), key = lambda x : x[1], reverse =True)
             
    answer = 0
    for size, cnt in new_arr:
        k -= cnt
        answer +=1
        if k <=0:
            break
                     
    return answer
    
    