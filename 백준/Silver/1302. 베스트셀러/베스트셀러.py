def solve():
    N = int(input())
    dict_book = {}

    for _ in range(N):
        title = input().rstrip()
        dict_book[title] = dict_book.get(title, 0) +1

    sorted_books = sorted(dict_book.items(), key=lambda x: (-x[1], x[0]))
    print(sorted_books[0][0])

solve()