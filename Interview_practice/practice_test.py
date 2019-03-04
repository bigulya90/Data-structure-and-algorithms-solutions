def merge(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid+1:]

        merge(left)
        merge(right)

        left_index = 0
        right_index = 0
        result_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                alist[result_index] = left[left_index]
                left_index += 1
            else:
                alist[result_index] = right[right_index]
                right_index += 1
            result_index += 1

        while left_index < len(left):
            alist[result_index] = left[left_index]
            left_index += 1
            result_index += 1

        while right_index < len(right):
            alist[result_index] = right[right_index]
            right_index += 1
            result_index += 1

        return alist



        