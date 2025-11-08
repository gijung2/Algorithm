def print_rev(temp):
    result = temp[::-1]
    return print(result)

def is_pal(temp):
    if temp == temp[::-1]:
        return print("입력하신 단어는 회문(Palindrome)입니다.")
    
word = input()
print_rev(word)
is_pal(word)