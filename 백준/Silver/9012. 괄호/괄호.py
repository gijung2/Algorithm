T=int(input())

for _ in range(T):
    s = input().strip()
    stack = []
    ok = True

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                ok = False
                break
            stack.pop()
    
    if ok and not stack:
        print("YES")
    else:
        print("NO")
        