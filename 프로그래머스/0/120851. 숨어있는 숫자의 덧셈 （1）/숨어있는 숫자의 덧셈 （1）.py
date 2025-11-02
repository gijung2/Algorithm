def solution(my_string):
    answer = []
    for ch in my_string:
        if ch.isdigit():
            answer.append(int(ch))
    sum = 0
    for i in answer:
        sum+=i
    return sum