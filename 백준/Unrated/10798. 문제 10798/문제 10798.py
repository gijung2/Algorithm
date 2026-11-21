arr = [list(input()) for _ in range(5)]

result =''
for j in range(15):
    for i in range(5):
        if j <len(arr[i]):
            result += arr[i][j]
            
print(result)
