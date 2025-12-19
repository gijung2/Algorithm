def solution(number, k):
    stack = []
    
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 아직 제거 못한 게 남아있으면 뒤에서 제거
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)
