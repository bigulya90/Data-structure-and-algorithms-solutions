def insertionSort(arr):
    for i in range(1, len(arr)): # iterate from 1 index to the end
        value = arr[i]

        # shift number to right, if it is greater then value
        temp = i - 1
        while temp >= 0 and value < arr[temp]:
            arr[temp + 1] = arr[temp]
            temp -= 1
        arr[temp + 1] = value


if __name__ == "__main__":
    arr = [2,5,3,1]
    insertionSort(arr)
    print ("Sorted array is:", arr)
