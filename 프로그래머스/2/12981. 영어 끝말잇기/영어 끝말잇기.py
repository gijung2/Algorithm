def solution(n, words):
    
    used = set()
    used.add(words[0])
    prev = words[0]
    
    for i in range(1,len(words)):
        word = words[i]
        
        if prev[-1] != word[0]:
            person = (i%n)+1
            turn = (i//n)+1
            return [person, turn]
        
        if word in used:
            person = (i%n)+1
            turn = (i//n)+1
            return [person, turn]
        
        used.add(word)
        prev = word
        
    return[0,0]
        
        