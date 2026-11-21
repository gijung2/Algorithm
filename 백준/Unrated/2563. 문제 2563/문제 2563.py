T = int(input())  # 색종이 개수

paper = [[0] * 100 for _ in range(100)]
result = 0

for _ in range(T):
    x, y = map(int, input().split())
    
    for r in range(x, x + 10):
        for c in range(y, y + 10):
            paper[r][c] = 1

for r in range(100):
    for c in range(100):
        if paper[r][c] == 1:
            result += 1

print(result)
