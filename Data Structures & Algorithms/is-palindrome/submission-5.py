class Solution:
    def isPalindrome(self, s: str) -> bool: 
        
        clean = []
        for c in s:
            if c.isalnum():
                clean.append(c)

        left = 0
        right = len(clean) - 1
        
        while left < right:
            if clean[left].lower() != clean[right].lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True 
        

        
        