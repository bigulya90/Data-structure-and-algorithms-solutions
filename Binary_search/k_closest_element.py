import collections


def findClosestElements(arr, k, x):

    def binary_search(a, target):
        low, high = 0, len(a) - 1
        while low != high:
            middle = int((low + high) / 2)
            if a[middle] > target:
                high = middle
            elif a[middle] < target:
                low = middle + 1
            else:
                return middle
        return low

    index = binary_search(arr, x)
    answers = collections.deque()
    low, high = index - 1, index

    while k > 0:
        if low < 0:
            answers.extend(arr[high:high + k])
            break
        elif high > len(arr) - 1:
            answers.extendleft(arr[low:low - k:-1])
            break
        elif ((x - arr[low]) > (arr[high] - x)):
            answers.append(arr[high])
            high += 1
        else:
            answers.appendleft(arr[low])
            low -= 1
        k -= 1
    return list(answers)


print (findClosestElements([1,2,3,4,5], k=4, x=3))