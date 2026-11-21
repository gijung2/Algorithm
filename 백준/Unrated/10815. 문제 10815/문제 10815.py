N= int(input())

arr1 = set(map(int,input().split()))

M= int(input())

arr2 = list(map(int,input().split()))


result = []

for x in arr2:
    if x in arr1:
        result.append("1")
    else:
        result.append("0")
        
print(' '.join(result))




