class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            j = len(nums) - 1
            k = i + 1
            rem = -nums[i]

            while k < j:
                sum1 = nums[k] + nums[j]

                if sum1 == rem:
                    out.append([nums[i], nums[k], nums[j]])

                    k += 1
                    j -= 1
                    while k < j and nums[k] == nums[k - 1]:
                        k += 1
                    while k < j and nums[j] == nums[j + 1]:
                        j -= 1

                elif sum1 > rem:
                    j -= 1
                else:
                    k += 1

        return out