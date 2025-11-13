from collections import Counter

def solution(N, stages):
    
#만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
#스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
#전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

# 로직 1. 개수를 센다 -> 2. 개수를 바탕으로 실패율을 계산 -> 3. 제한사항들을 구현
    
    count = Counter(stages) #딕셔너리로 저장
    players = len(stages)
    
    failure = []
    
    for stage in range(1,N+1):
        if players == 0:
            failure.append((stage,0))
            continue
        
        fail = count[stage] / players
        failure.append((stage, fail))
        
        players -= count[stage]
        
    failure.sort(key=lambda x: (-x[1], x[0]))
    
    return [stage for stage, _ in failure]
    