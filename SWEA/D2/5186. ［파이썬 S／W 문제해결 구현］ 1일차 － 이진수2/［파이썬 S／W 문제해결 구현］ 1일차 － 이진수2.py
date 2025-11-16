T = int(input())

def binary_change(n):

    cnt =0
    result = ''
    a = 1

    while n:
        if n< 2**-a:
            result +='0'
        else:
            n -= 2**-a
            result+='1'
        
        cnt+=1
        if cnt>12:
            return 'overflow'
        
        else:
            a+=1
    
    return result

for tc in range(1,T+1):
    N = float(input())
    print("#{} {}".format(tc,binary_change(N)))