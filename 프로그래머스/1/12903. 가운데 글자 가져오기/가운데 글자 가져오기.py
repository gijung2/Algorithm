def solution(s):
    answer = ''
    temp=[]
    chm = len(s)
    if chm % 2 == 0:
        temp.append(s[chm//2-1])
        temp.append(s[chm//2])
    else:
        temp = s[chm//2]
    return answer.join(temp)