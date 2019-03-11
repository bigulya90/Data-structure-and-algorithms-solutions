"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target,
find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'
"""


class Solution:
    def find_letter(self, letters, target):
        if target > letters[-1]:
            return letters[0]

        left = 0
        right = len(letters)-1

        while left < right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1

        return letters[left]


