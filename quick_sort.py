# """
# Autor: Bradley Miller. Problem solving with DSA using Python. Second edition.
# """
#
#
# def quickSort(alist):
#    quickSortHelper(alist,0,len(alist)-1)
#
#
# def quickSortHelper(alist,first,last):
#    if first < last:
#
#        splitpoint = partition(alist,first,last)
#
#        quickSortHelper(alist,first,splitpoint-1)
#        quickSortHelper(alist,splitpoint+1,last)
#
#
# def partition(alist,first,last):
#    pivotvalue = alist[first]
#
#    leftmark = first+1
#    rightmark = last
#
#    done = False
#    while not done:
#
#        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
#            leftmark = leftmark + 1
#
#        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
#            rightmark = rightmark -1
#
#        if rightmark < leftmark:
#            done = True
#        else:
#            temp = alist[leftmark]
#            alist[leftmark] = alist[rightmark]
#            alist[rightmark] = temp
#
#    temp = alist[first]
#    alist[first] = alist[rightmark]
#    alist[rightmark] = temp
#
#
#    return rightmark
#
# alist = [54,26,93,17,77,31,44,55,20]
# quickSort(alist)
# print(alist)
#
#
#
#
#
#
#
#
def partition(alist, first, last):
    pivot_value = alist[first]

    left = first + 1
    right = last

    done = False

    while not done:

        while alist[left] <= pivot_value and left <= right:
            left = left + 1

        while alist[right] >= pivot_value and right >= left:
            right -= 1

        if left > right:
            done = True
        else:
            temp = alist[left]
            alist[left] = alist[right]
            alist[right] = temp

    temp = alist[first]
    alist[first] = alist[right]
    alist[right] = temp

    return right

def sortHelper(alist, first, last):

    position = partition(alist, first, last)

    sortHelper(alist, first, position-1)
    sortHelper(alist, position + 1, last)


def quickSort(alist):
    sortHelper(alist, 0, len(alist)-1)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)










































