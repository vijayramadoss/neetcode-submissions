class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      d={}
      res=0
      l=0
      m=0
      for r in range(len(s)):
        d[s[r]]=1+d.get(s[r],0)
        m=max(m,d[s[r]])
        while(r-l+1)-m >k:
            d[s[l]]-=1
            if d[s[l]] == 0:
                del d[s[l]]
            l+=1
        res=max(res,r-l+1)
      return res
        

        

