def solution(s):
    answer = len(s)

    for size in range(1, len(s)//2 + 1):
        compress = 0
        prev = s[0:size]
        count = 1

        for i in range(size, len(s), size):
            curr = s[i:i+size]

            if prev == curr:
                count += 1
            else:
                if count > 1:
                    compress += size + len(str(count))
                else:
                    compress += len(prev)

                prev = curr
                count = 1

        if count > 1:
            compress += size + len(str(count))
        else:
            compress += len(prev)

        answer = min(answer, compress)

    return answer
