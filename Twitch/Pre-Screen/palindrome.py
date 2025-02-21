def solution(inputString):
    
    palindrome = inputString.lower()
    
    if palindrome == palindrome[::-1]:
        return True
    else:
        return False
        