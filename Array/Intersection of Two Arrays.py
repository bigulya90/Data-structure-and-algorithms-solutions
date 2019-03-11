# Given two arrays, write a function to compute their intersection.


class Solution:
    def find_intersaction(self, num1, num2):
        if len(num1) <= 0 or len(num2) <= 0:
            return -1

        word = {}
        result = []

        for i in num1:
            word[i] = word.get(i, 0) + 1

        for i in num2:
            if i in word and word.get(i, 0) > 0:
                result.append(i)
                word[i] -= 1
        return result
    