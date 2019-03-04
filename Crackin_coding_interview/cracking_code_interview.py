"""1. Write algorithm to determine if a string has all unique char"""


def is_unique(string_input):
    if len(string_input) == 0:
        return None

    hash_set = set()

    for char in string_input:
        if char in hash_set:
            return False
        else:
            hash_set.add(char)
    return True


print(is_unique("Biga"))


"""2. Check permutation"""
def checker(st1, st2):
    if len(st1) != len(st2):
        return False

    # ord() - int representing of unicode
    char_count = [0] * 256
    for c in st1:
        char_count[ord(c)] += 1

    for c in st2:
        char_count[ord(c)] -= 1
        if char_count[ord(c)] != 0:
            return False
    return True

st1 = "biga"
st2 = "vvfg"
print (checker(st1, st2))

def if_two_words_are_permutations(s1, s2):
    if len(s1) != len(s2):
        return False
    dic = {}
    for ch in s1:
        if ch in dic.keys():
            dic[ch] += 1
        else:
            dic[ch] = 1
    for ch in s2:
        if ch not in dic.keys():
            return False
        elif dic[ch] == 0:
            return False
        else:
            dic[ch] -= 1
    return True


print (if_two_words_are_permutations("biga", "dani"))


"""3. Replace space with %"""
def replace_token_inplace(s, token=" "):
    for char in s:
        if ord(char) == ord(token):
            yield "20%"
        else:
            yield char


replace_token_inplace("biga a girl")


"""4. Palindrome permutation"""
def Palindrome_permutation(the_string):
    unpair_char = set()
    if len(the_string) == 0:
        return None

    for char in the_string:
        if char in unpair_char:
            unpair_char.remove(char)
        else:
            unpair_char.add(char)
    return len(unpair_char) <= 1

print (Palindrome_permutation("biga"))


"""5. one way edit"""
def one_way(st1, st2):

    count = [0] * 256
    for char in st1:
        count[ord(char)] += 1

    for char in st2:
        count[ord(char)] -= 1
        if count[ord(char)] >= 1:
            return False
    return True


print (one_way("biga", "biki"))


"""6. String compression"""
def compression(the_string):
    count = 0
    for i in range(len(the_string)):
        if the_string[i] == the_string[i + 1]:
            count += 1
        else: break
    return the_string

compression("aabbbccc")


"""7. Rotate matrix positive 90"""
def matrix(mat):
    l = len(mat[0])
    m = l // 2

    for x in range(l-1):
        for y in range(l-x-1):
            mat[x][y], mat[l-y-1][l-x-1] = mat[l-y-1][l-x-1], mat[x][y]

    for i in range(m):
        mat[i], mat[l-i-1] = mat[l-i-1], mat[i]


def negative_rotation(mat):
    n = len(mat)
    for x in range(0, n-1):
        for y in range(x, n-1-x):
            temp = mat[x][y]
            mat[x][y] = mat[y][n-1-x]
            mat[y][n-1-x] = mat[n-1-x][n-1-y]

            mat[n - 1 - x][n - 1 - y] = mat[n-1-y][x]
            mat[n - 1 - y][x] = temp

"""8. String rotation"""
"""9. Zero matrix"""
# Linked List
"""10. Remove duplicates in unsorted LL"""









