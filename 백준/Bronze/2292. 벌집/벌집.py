N = int(input())

count = 1
end = 1

while N > end:
    end += 6 * count
    count +=1
    
print(count)