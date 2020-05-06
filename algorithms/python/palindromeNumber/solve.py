class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        strx = str(x)
        rx = strx[::-1] 
        
        return int(rx) == x