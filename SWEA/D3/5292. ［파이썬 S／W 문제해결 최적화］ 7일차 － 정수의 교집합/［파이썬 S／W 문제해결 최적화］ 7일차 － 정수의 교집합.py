T = int(input())

for i in range(1, T+1):
    N, M = map(int,input().split())
    
    A= set(map(int,input().split()))
    B= set(map(int,input().split()))
    
    ans = len(A&B)
    
    print(f'#{i} {ans}')