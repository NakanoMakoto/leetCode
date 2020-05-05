class Solution:
    def reverse(self, x: int) -> int:
        strx = str(x)
        ans = ""
        
        if x >= 0:
            ans = strx[::-1]
        else:
            tmp = strx[1:]
            ans = "-" + tmp[::-1]
        
        if int(ans) >= 2**31-1 or int(ans) <= -2**31: return 0
        else: return int(ans)