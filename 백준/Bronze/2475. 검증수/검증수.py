nums = list(map(int, input().split()))

def nums_two(nums):
    total = 0
    for i in nums:
        total += i **2
    return total
result = nums_two(nums) % 10
print("%d" %(result))