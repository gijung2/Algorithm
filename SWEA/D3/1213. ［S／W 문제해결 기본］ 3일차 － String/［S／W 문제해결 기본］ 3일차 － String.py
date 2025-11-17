for _ in range(10):
    tc = int(input().strip())
    pattern = input().strip()
    text = input().strip()

    m = len(pattern)
    tl = len(text)

    cnt =0
    for ch in range(tl-m+1):
        if text[ch:ch+m] ==pattern:
            cnt+=1


    print("#{} {}".format(tc,cnt))