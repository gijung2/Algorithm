T = int(input())
lis = []  # 약수를 저장할 리스트

for i in range(1, T + 1):
    if T % i == 0:
        print(f"{i}(은)는 {T}의 약수입니다.")
        lis.append(i)

# 약수가 2개뿐이라면 소수
if len(lis) == 2:
    print(f"{T}(은)는 {lis[0]}과 {lis[1]}로만 나눌 수 있는 소수입니다.")
