from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Appears more than n/2 times
        # It is always in the array
        threshold = len(nums) / 2
        tracker_dict = {}
        for num in nums:
            if num in tracker_dict:
                tracker_dict[num] += 1
            else:
                tracker_dict[num] = 1
            if tracker_dict[num] > threshold:
                return num


nums = [3, 2, 3]
result = Solution().majorityElement(nums=nums)
