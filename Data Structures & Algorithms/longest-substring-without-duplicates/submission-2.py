class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in long:
                long.remove(s[l])
                l+=1
            long.add(s[r])
            res=max(res,len(long))
        return res
            
        
            
        