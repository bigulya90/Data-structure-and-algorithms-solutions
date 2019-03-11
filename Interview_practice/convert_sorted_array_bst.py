class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def convert_sorted_array_to_bst(self, nums):
        if not nums:
            return None

        if len(nums) == 1:
            return nums

        mid = (len(nums)) // 2

        root = TreeNode(nums[mid])
        
        root.left = self.convert_sorted_array_to_bst(nums[:mid])
        root.right = self.convert_sorted_array_to_bst(nums[mid+1:])
        return root

