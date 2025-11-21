from itertools import combinations
arr=[]
for _ in range(9):
    num = int(input())
    arr.append(num)
    
for c in combinations(arr,7):
    if sum(c)== 100:
        for h in sorted(c):
            print(h)
        break