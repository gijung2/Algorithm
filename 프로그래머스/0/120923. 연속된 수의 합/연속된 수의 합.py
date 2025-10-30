def solution(num, total):
    for start in range(-1000, 1001):
        seq = [start+i for i in range(num)]
        if sum(seq) == total:
            return seq
    answer = seq    
    return answer