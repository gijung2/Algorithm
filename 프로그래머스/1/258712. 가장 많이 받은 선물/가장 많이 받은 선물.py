def solution(friends, gifts):
    # 누가 누구에게 선물했는지를 저장
    gifted = {}  # {"friend": {"상대": 준 개수}}
    gift_idx = {}  # 선물 지수

    # 초기화
    for friend in friends:
        gifted[friend] = {}
        gift_idx[friend] = 0

    # 선물 기록 & 선물 지수 계산
    for gift in gifts:
        t, f = gift.split(' ')  # t: 준 사람, f: 받은 사람
        if f in gifted[t]:
            gifted[t][f] += 1
        else:
            gifted[t][f] = 1

        gift_idx[t] += 1
        gift_idx[f] -= 1

    # 다음 달에 받게 될 선물 개수
    will_get = [0 for _ in friends]

    # 친구 쌍 비교
    for i in range(len(friends)):
        curr = friends[i]
        for j in range(i + 1, len(friends)):
            another = friends[j]

            # curr → another
            a = gifted[curr][another] if another in gifted[curr] else 0
            # another → curr
            b = gifted[another][curr] if curr in gifted[another] else 0

            if a > b:
                will_get[i] += 1
            elif a < b:
                will_get[j] += 1
            else:  # a == b
                ai, bi = gift_idx[curr], gift_idx[another]
                if ai > bi:
                    will_get[i] += 1
                elif ai < bi:
                    will_get[j] += 1

    answer = max(will_get)
    return answer
