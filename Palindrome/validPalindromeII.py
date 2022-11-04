# 680. Valid Palindrome II


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.palindome(s[l:r]) or self.palindome(s[l + 1: r + 1])
        return True           
    
    def palindome(self, s):
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
