def IsPalindrome(s): 
    s = s.lower().replace(" ", "")
    return s == s[::-1]