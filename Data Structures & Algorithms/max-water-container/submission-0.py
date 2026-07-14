class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea=0
        m=0
        n=len(heights)-1
        while(m<n):
            area=(n-m)*min(heights[m],heights[n])
            maxarea=max(maxarea,area)
            if(heights[m]<heights[n]):
                m+=1
            elif(heights[m]>heights[n]):
                n-=1
            else:
                m+=1
        return maxarea