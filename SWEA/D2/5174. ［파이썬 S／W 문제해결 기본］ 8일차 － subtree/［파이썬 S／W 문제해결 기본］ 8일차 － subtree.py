def dfs(node):
    global count
    if node == 0:
        return
    count+=1
    dfs(left[node])
    dfs(right[node])

T= int(input())

for tc in range(1,T+1):
    E,N = map(int, input().split())
    data = list(map(int, input().split()))

    left = [0]*(E+2)
    right = [0]* (E+2)

    for i in range(0, len(data),2):
        parent = data[i]
        child = data[i+1]

        if left[parent] ==0:
            left[parent]= child
        else:
            right[parent] = child

    count = 0
    dfs(N)
    print(f'#{tc} {count}')