class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for i in range(len(strs)):
            k={chr(f): 0 for f in range(ord('a'), ord('z') + 1)}
            for j in strs[i]:
                k[j]+=1
            m=tuple(k.values())
            if m not in s:
                s[m]=[strs[i]]
            else:
                s[m].append(strs[i])
        f=list(s.values())
        return f
        
            
        
            
