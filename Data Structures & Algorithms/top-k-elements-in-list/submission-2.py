class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[[] for i in range(len(nums)+1)]
        s={}
        m=[]
        for i in (nums):
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        c=s.items()
        for i,j in c:
            l[j].append(i)
        for i in range(len(l)-1,0,-1):
            for j in l[i]:
                m.append(j)
                if len(m)==k:
                    return m
        