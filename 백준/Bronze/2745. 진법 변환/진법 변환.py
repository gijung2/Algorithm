N, B = input().split()
B = int(B)

result = 0

for ch in N:
    if '0'<= ch <='9':
        val = ord(ch) -ord('0')
    else:
        val = ord(ch) - ord('A')+10
        
    result = result*B + val
    
print(result)