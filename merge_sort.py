"""
Merge sort implementation in Python.
"""

def mergeSort(alist):
    print ("Splitting list ", alist)

    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        k = 0
        j = 0

        while (i < len(left) and j < len(right)):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while (i < len(left)):
            alist[k] = left[i]
            i += 1
            k += 1

        while (j < len(right)):
            alist[k] = right[j]
            j += 1
            k += 1

        print ("Merging list ", alist)


mergeSort([5,2,8,1,0,33,6,12])


