class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         m=0
         n=len(numbers)-1
         while(m<n):
            sum=numbers[m]+numbers[n]
            if sum == target:
                return [m+1,n+1]
            elif sum>target:
                n-=1
            else:
                m+=1
        