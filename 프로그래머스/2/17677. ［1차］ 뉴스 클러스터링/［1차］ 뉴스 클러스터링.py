from collections import Counter

def solution(str1, str2):
    
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_list = []
    str2_list = []
    
    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_list.append(str1_low[i]+str1_low[i+1])
            
    for i in range(len(str2_low)-1):
        if str2_low[i].isalpha() and str2_low[i+1].isalpha():
            str2_list.append(str2_low[i]+str2_low[i+1])
            
            
    counter1 = Counter(str1_list) 
    counter2 = Counter(str2_list)
    
    inter = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())
    
    if len(union) == 0 and len(inter) ==0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
            
            
            
            
            
            
            