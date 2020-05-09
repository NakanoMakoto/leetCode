class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        m = {"(": ")", "{": "}", "[": "]"}
        t = set(["(", "{", "["])
        
        for v in s:
            if v in t:
                l.append(v)
            elif l and v == m[l[-1]]:
                l.pop()
            else:
                return False
        return len(l) == 0