"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

"""


def findDuplicate(nums):
    low = 0
    high = len(nums) - 1
    mid = (high + low) / 2

    while high - low > 1:
        count = 0
        for k in nums:
            if mid < k <= high:
                count += 1
        if count > high - mid:
            low = mid
        else:
            high = mid
        mid = (high + low) / 2

    return high


print findDuplicate([1,2,3,4,5,6, 6, 6])






































