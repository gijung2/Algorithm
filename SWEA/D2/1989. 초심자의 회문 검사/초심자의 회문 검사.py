T = int(input().strip())

for i in range(1, T+1):
    exam = input().strip()

    reverse = exam[::-1]
    if exam == reverse:
        print(f"#{i} {1}")
    else:
        print(f"#{i} {0}")