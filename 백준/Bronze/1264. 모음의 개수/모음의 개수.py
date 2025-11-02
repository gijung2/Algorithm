while True:
    line = input()
    if line == '#':  # 종료 조건
        break

    vowels = 'aeiouAEIOU'  # 대소문자 포함
    count = 0

    for ch in line:
        if ch in vowels:
            count += 1

    print(count)
