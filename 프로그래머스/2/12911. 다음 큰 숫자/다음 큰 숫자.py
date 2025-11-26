def solution(n):
    answer = 0
    #범위는 n보다 큰 범위로 잡아서 while문을 돌리고
    #2진수로 변환하는데, 변환한 문자열에서 coutn메소드를사용하여 1의개수를체크
    n_bi = bin(n)[2:]
    n_cn = n_bi.count("1")
    while 1:
        n+=1
        chanbi = bin(n)[2:]
        chanbi_cn = chanbi.count("1")
        if n_cn == chanbi_cn:
            return n
            
    
    
    