# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

def anagram(s1: str, s2: str) -> bool:
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for i in s1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in s2:
        if i in count:
            count[i] -= 1
        else:
            count[i] = 1

    for i in count:
        if count[i] != 0:
            return False

    return True

print(anagram("anagram", "nagaram"))
print(anagram("anagram", "nagaram"))
print(anagram("rat", "car"))
