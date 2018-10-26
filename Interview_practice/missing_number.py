"""
If you have an unsorted array of numbers from 1-100, except 1 of those numbers is missing, how do you determine
which number is missing
"""

def function(arr):
    start = 1
    end = len(arr)

    result = end*(end-start)/2 - sum(end, start)
    return result

print function([1, 2, 3, 4, 5, 7, 8, 9, 10])
