"""Find the intersection of two arrays

Solutions:
1. sort 2 arrays and use binary search in short array
2. sort and use built-in function set
3. find the longest array, add to hash to fast lookup and loop the short"""


def function(ar1, ar2):
    # TODO: find the longest array
    s = set(ar1)
    return list({i for i in ar2 if i in s})
