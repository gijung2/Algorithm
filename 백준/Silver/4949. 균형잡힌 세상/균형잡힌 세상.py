while True:
    s = input()
    if s == '.':
        break

    stack = []
    check = True
    
    for ch in s:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                check = False
                break
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                check = False
                break
            stack.pop()

    if check and not stack:
        print("yes")
    else:
        print("no")
