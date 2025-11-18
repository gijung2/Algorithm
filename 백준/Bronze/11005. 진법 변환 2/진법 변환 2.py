N, B = map(int, input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while N > 0:
    result += digits[N % B]  # 나머지에 해당하는 문자를 추가
    N //= B                  # N을 B로 나누어 갱신

print(result[::-1])          # 역순으로 뒤집어서 출력
