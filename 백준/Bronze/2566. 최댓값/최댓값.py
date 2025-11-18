arr = [list(map(int, input().split())) for _ in range(9)]

max_val = -1
x = y = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            x, y = i, j

print(max_val)
print(x+1, y+1)   # 문제는 1-based index 요구
