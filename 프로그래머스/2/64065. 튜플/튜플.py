from collections import defaultdict

def solution(s):
    s = s[2:-2]
    
    counter = defaultdict(int)
    sets=s.split('},{')
    
    final =[]
    for part in sets:
        nums = part.split(",")
        
        for n in nums:
            counter[int(n)] += 1

        
    answer = sorted(counter, key=lambda x: counter[x],reverse=True)
    return answer