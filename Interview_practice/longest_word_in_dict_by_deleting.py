"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting
some characters of the given string. If there are more than one possible results, return the longest word with the
smallest lexicographical order. If there is no possible result, return the empty string.
"""


def findLongestWord(s, d):
    res = ""
    for word in d:  # O(|d|)
        if isSubseq(s, word):  # O(|s|)
            if len(word) > len(res):
                res = word
            elif len(word) == len(res):
                res = res if res < word else word  # lexigraphical comparison
    return res


def isSubseq(string, sub):
    subIdx = 0
    for c in string:
        if subIdx == len(sub):  # means we've traversed the entire subsequence
            break
        if sub[subIdx] == c:
            subIdx += 1
    return subIdx == len(sub)


s = "abpcplea"
d = ["ale","apple","monkey","plea"]

findLongestWord(s, d)



