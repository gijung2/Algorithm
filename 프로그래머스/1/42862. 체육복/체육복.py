def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    
    # 1. 자기 여벌로 자기 해결
    overlap = lost & reserve
    lost -= overlap
    reserve -= overlap
    
    # 2. 작은 번호부터 처리
    for student in sorted(lost):
        if student - 1 in reserve:
            reserve.remove(student - 1)
        elif student + 1 in reserve:
            reserve.remove(student + 1)
        else:
            n -= 1  # 못 빌림
    
    return n
