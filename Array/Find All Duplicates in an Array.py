class Solution:
    def find_duplicates(self, nums):
        word = {}
        result = []

        for i in nums:
            if i in word:
                word[i] += 1
            else:
                word[i] = 1

        for i in word:
            if word.get(i, 0) >= 2:
                result.append(i)

        return result
    