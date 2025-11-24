def solution(s):
    sta = []
    for ch in s:
        
        if ch == '(':
            sta.append(ch)
        else:
            if not sta:
                return False
            sta.pop()
    
    return len(sta) == 0