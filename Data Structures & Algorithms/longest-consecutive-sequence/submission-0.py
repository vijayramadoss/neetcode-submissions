class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s={}
        out=0
        l=len(nums)
        for i in range(l):
            s[nums[i]]=s.get(nums[i],0)+1
        for i in nums:
            if i-1 not in s:
                count=1
                cur=i
                while(True):
                    if(cur+1 in s):
                        count+=1
                        cur=cur+1
                    else:
                        out=max(out,count)
                        break
            else:
                continue
        return out
