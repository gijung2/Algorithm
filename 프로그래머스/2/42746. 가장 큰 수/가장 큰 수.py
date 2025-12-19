def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x: x*3, reverse = True)
    
    result = ''.join(numbers)
    
    if result[0] == '0':
        return '0'
    else:
        return result