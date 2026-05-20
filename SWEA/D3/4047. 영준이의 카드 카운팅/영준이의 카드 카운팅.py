


T = int(input())

for tc in range(1, T+1):

    dic ={
    "S": 13,
    "D": 13,
    "H": 13,
    "C": 13,
    }
    

    ab = input()
    length = len(ab)
    ss =set()

    answer = "ERROR"
    for i in range(0, length, 3):
        ss.add(ab[i:i+3])

    if len(ss) != length//3:
        answer = "ERROR"

    else:
        for s in ss:
            dic[s[0]] -=1
    
        answer = " ".join(map(str, dic.values()))

    print(f"#{tc} {answer}")

    