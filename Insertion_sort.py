

def insertion_sort(alist):
    if len(alist) == 1:
        return alist

    if len(alist) == 0:
        raise ValueError ("list is empty")

    for index in range(1, len(alist)):
        value_to_shift = alist[index]
        position = index

        while position > 0 and alist[position -1] > value_to_shift:
            alist[position] = alist[position -1]
            position = position - 1

        alist[position] = value_to_shift



if __name__ == "__main__":
    arr = [2,5,3,1, 0, 8, 4]
    insertion_sort(arr)
    print ("Sorted array is:", arr)


