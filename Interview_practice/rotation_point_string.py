"""
Write a function for finding the index of the "rotation point," which is where I started working from the beginning of
the dictionary. This list is huge (there are lots of words I don't know) so we want to be efficient here.
"""


def rotation_points(word):
    first_word = word[0]
    left = 0
    right = len(word) - 1

    while left < right:
        #mid = left + ((right - left) / 2)
        mid = (left + right) / 2

        if word[mid] >= first_word:
            left = mid
        else:
            right = mid

        if left + 1 == right:
            return right


word = ['k', 'v', 'a', 'b', 'c', 'd', 'e', 'g', 'i']
numbers = [4, 5, 6, 1, 2, 3]
print (rotation_points(word))

