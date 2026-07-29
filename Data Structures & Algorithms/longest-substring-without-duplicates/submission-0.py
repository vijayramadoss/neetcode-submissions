class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k=set()
        l=0
        res=0
        for r in range(len(s)):
            while(s[r] in k):
                k.remove(s[l])
                l+=1
            k.add(s[r])
            res=max(res,r-l+1)
        return res