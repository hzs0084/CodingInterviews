def palindrome(s1: str) -> bool:
    s1 = s1.lower()

    return s1 == s1[::-1]

print(palindrome("racecar"))