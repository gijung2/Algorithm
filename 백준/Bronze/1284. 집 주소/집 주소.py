import sys

for line in sys.stdin:
    n = line.strip()  # 줄 끝 개행 제거

    # 입력의 마지막은 0 한 줄이고, 이건 처리하지 말고 종료
    if n == "0":
        break

    # 맨 왼쪽 여백 1cm
    total = 1

    # 각 숫자 처리
    for ch in n:
        if ch == '1':
            total += 2      # 숫자 1의 폭
        elif ch == '0':
            total += 4      # 숫자 0의 폭
        else:
            total += 3      # 나머지 숫자의 폭 (2~9)
        total += 1          # 숫자 뒤 여백 1cm (마지막 숫자 뒤 여백 = 오른쪽 여백)

    print(total)
