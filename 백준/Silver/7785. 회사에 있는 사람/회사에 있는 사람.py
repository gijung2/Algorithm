N = int(input())

arr = set()

for _ in range(N):
    name, log = input().split()

    if log == 'enter':
        arr.add(name)
    else:
        arr.remove(name)

arr = sorted(arr, reverse=True)

for ch in arr:
    print(ch)