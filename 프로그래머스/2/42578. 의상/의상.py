def solution(clothes):
    #매일 다른 옷을 입어야됨
    #각 종류별로 최대 1가지 의상만 착용 가능, 일부의 착용 의상이 겹치더라도
    #다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법
    #방법: 추가로 입기, 한 종류의 의상이 여러벌인 경우 그 한 종류에서 여러벌을 다르게 입기
    answer = 1
    closet ={}
    for name, kind in clothes:
        if kind in closet:
            closet[kind] +=1
        else: 
            closet[kind] = 1
            
    for k in closet:
            
        answer *= (closet[k]+1)
            
    return answer -1