T = int(input())
for tc in range(1, T + 1):
    str1 = input().strip()
    str2 = input().strip()

    # 각 문자 카운트 저장용 딕셔너리
    count_dict = {}

    for ch in str1:  # str1에 있는 문자만 조사
        count_dict[ch] = str2.count(ch)  # str2 안에 몇 개 있는지 세기

    # 딕셔너리에서 가장 큰 값(최댓값)
    ans = max(count_dict.values())

    print(f"#{tc} {ans}")
