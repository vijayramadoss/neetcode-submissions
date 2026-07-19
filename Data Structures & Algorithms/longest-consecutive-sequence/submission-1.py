class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         if not nums:
            return 0

         s = set(nums)
         out = 0

         for i in s:
            if i - 1 not in s:
                count = 1
                cur = i

                while cur + 1 in s:
                    cur += 1
                    count += 1

                out = max(out, count)

         return out
