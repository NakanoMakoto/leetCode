class Solution:
    def romanToInt(self, s: str) -> int:
        """
        A = 4
        B = 9
        
        E = 40
        F = 90
        
        G = 400
        H = 900
        """
        
        s = s.replace('IV', 'A')
        s = s.replace('IX', 'B')
        
        s = s.replace('XL', 'E')
        s = s.replace('XC', 'F')
        
        s = s.replace('CD', 'G')
        s = s.replace('CM', 'H')
        
        ans = 0
        for v in s:
            if v == 'A':
                ans += 4
            elif v == 'B':
                ans += 9
            elif v == 'C':
                ans += 100
            elif v == 'D':
                ans += 500
            elif v == 'E':
                ans += 40
            elif v == 'F':
                ans += 90
            elif v == 'G':
                ans += 400
            elif v == 'H':
                ans += 900
            elif v == 'I':
                ans += 1
            elif v == 'L':
                ans += 50
            elif v == 'M':
                ans += 1000
            elif v == 'X':
                ans += 10
            elif v == 'V':
                ans += 5
        return ans