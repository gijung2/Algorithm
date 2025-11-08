numbers = []  # 입력받은 수들을 저장할 리스트

for i in range(9):
    num = int(input())  # 한 줄씩 입력받기
    numbers.append(num)  # 리스트에 추가

max_value = max(numbers)          # 최댓값 구하기
max_index = numbers.index(max_value) + 1  # 몇 번째 수인지 (인덱스는 0부터라 +1)

print(max_value)
print(max_index)
