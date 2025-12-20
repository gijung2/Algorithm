def digit_sum(s):
    total = 0
    for c in s:
        if c.isdigit():
            total += int(c)
    return total
N = int(input())

arr = [input().strip() for _ in range(N)]

arr.sort(key=lambda x: (len(x) , digit_sum(x) , x))


for x in arr:
    print(x)