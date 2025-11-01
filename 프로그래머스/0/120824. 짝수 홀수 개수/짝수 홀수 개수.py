def solution(num_list):
    answer = []
    jjak = 0
    for i in num_list:
        if i % 2 == 0:  # 짝수 확인
            jjak += 1
    answer.append(jjak)  # 짝수 개수
    answer.append(len(num_list) - jjak) 
    return answer
