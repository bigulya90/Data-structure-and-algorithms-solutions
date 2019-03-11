"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

"""

class Solution:
    def find_min(self, nums):
        if len(nums) == 1:
            return nums

        if len(nums) == 0:
            return None

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if left == right:
                return nums[mid]

            if nums[mid] > nums[right]:
                right = mid
            else:
                left = mid + 1


