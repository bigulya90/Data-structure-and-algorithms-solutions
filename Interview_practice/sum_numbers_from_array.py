# return a list of lists of length 3


def three_Sum(num):
    if len(num) < 3: return []

    num.sort()
    result = []

    for i in range(len(num) - 2):
        left = i + 1
        right = len(num) - 1
        if i != 0 and num[i] == num[i - 1]: continue
        while left < right:
            if num[left] + num[right] == -num[i]:
                result.append([num[i], num[left], num[right]])
                left = left + 1
                right = right - 1
                while num[left] == num[left - 1] and left < right: left = left + 1
                while num[right] == num[right + 1] and left < right: right = right - 1
            elif num[left] + num[right] < -num[i]:
                left = left + 1
            else:
                right = right - 1
    return result


nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [-25, -10, -7, -3, 2, 4, 8, 10]
print(three_Sum(nums1))
print(three_Sum(nums2))



# function to print triplets with 0 sum

def findTriplets(arr, n):
    found = False

    # sort array elements
    arr.sort()

    for i in range(0, n - 1):

        # initialize left and right
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l < r):


            if (x + arr[l] + arr[r] == 0):
                # print elements if it's sum is zero
                print(x, arr[l], arr[r])
                l += 1
                r -= 1
                found = True


            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[l] + arr[r] < 0):
                l += 1

            # if sum is greater than zero than
            # decrement in right side
            else:
                r -= 1

    if (found == False):
        print(" No Triplet Found")


def sum_numbers_itterative(arr_number):
    sum_res = 0

    for i in arr_number:
        sum_res += i
    return sum_res


def sum_num_rec(arr_num):
    if len(arr_num) == 1:
        return arr_num[0]

    else:
        return arr_num[0] + sum_num_rec(arr_num[1:])