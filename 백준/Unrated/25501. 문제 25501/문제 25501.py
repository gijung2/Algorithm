def recursion(s, l, r, cnt):
    cnt[0] += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1, cnt)
    
def ispallin(s, cnt):
    return recursion(s, 0, len(s)-1, cnt)

T= int(input())

for _ in range(T):
    s = input().strip()
    cnt = [0]
    result = ispallin(s, cnt)
    
    print(result, cnt[0])