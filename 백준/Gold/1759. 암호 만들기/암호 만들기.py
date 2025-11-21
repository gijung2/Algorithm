from itertools import combinations

L,C = map(int,input().split())
arr =sorted(input().split())

vowels = {'a','e','i','o','u'}

for combo in combinations(arr,L):
    cnt_v=0
    cnt_c=0
    
    for ch in combo:
        if ch in vowels:
            cnt_v+=1
        else:
            cnt_c+=1
            
            
    if cnt_v >=1 and cnt_c >=2:
        print("".join(combo))