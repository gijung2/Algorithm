def solution(quiz):
    answer = []
    for q in quiz:
        x, op, y, _, z = q.split()   # "3 - 4 = -1" → ['3', '-', '4', '=', '-1']
        x, y, z = int(x), int(y), int(z)

        if op == '+':
            answer.append('O' if x + y == z else 'X')
        else:
            answer.append('O' if x - y == z else 'X')
    return answer
