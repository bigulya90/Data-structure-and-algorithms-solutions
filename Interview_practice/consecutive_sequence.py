"""
Given unsorted array.
Find the len of the longest consecutive sequence
[1, 2, 3, 4, 7] --> 4

"""


def consecutive(alist):
    hash_list = set()
    count_num = 0

    for i in alist:
        hash_list.add(i)

    length = len(alist)

    for j in range(length):
        if alist[j]-1 not in hash_list:
            temp = alist[j]

            while(temp in hash_list):
                temp +=1
            count_num = max(count_num, temp - alist[j])

    return count_num


print (consecutive([1, 2, 3]))














