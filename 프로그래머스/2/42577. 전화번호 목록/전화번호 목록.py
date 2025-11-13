def solution(phone_book):
    hash_map = {}
    
    for number in phone_book:
        hash_map[number] = True
        
    for number in phone_book:
        for i in range(1,len(number)):
            prefix = number[:i]
            if prefix in hash_map:
                return False
            
    return True