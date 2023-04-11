# Palindrome function

def palindrome(s):
    print(s[::-1])
    print(s)
    if s == s[::-1]:
        return True
    else:
        return False
    
palindrome("rent")
