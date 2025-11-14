from itertools import permutations

def checkPrime(n):
    if n <2:
        return False
    
    for i in range(2, int(n** 0.5) +1):
        if n % i ==0:
            return False
        
    return True

def solution(numbers):
    answer = []
    numbers = list(numbers)
    num = []
    
    for i in range(1, len(numbers)+1):
        num.append(list(permutations(numbers,i)))
    
    new_num = []
    for group in num:
        for item in group:
            number = int(''.join(item))
            new_num.append(number)
            
    num = new_num
    
    for i in num:
        
        if checkPrime(i):
            answer.append(i)
            
    return len(set(answer))