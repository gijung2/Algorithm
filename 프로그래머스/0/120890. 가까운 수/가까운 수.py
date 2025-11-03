def solution(array, n):
    # 1️⃣ array를 오름차순으로 정렬 (같은 거리일 때 더 작은 수 선택용)
    array.sort()

    # 2️⃣ 각 원소와 n의 차이(거리)를 계산해서 가장 가까운 값을 찾기
    answer = min(array, key=lambda x: abs(x - n))

    return answer
