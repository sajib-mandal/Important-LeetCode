# 125. Valid Palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            elif l < r and not self.alphaNum(s[l]):
                l += 1
            elif r > l and not self.alphaNum(s[r]):
                r -=1
            else:
                return False
        return True
    
    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))
    
    
    
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            elif not self.alphaNum(s[l]):
                l += 1
            elif not self.alphaNum(s[r]):
                r -=1
            else:
                return False
        return True
    
    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))
