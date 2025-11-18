N = int(input())

words = set()   # 중복 제거용

for _ in range(N):
    words.add(input().strip())

# 길이 기준 → 사전순 기준
words = sorted(words, key=lambda x: (len(x), x))

for w in words:
    print(w)
