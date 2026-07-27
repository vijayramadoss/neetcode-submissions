class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        s=nums[:]
        for i in range(n):
                 s[(i+k)%n]=nums[i]
        nums[:]=s