"""
in general, an in-place algo requares the swap method
O(n) time and O(1)O(1) space.
"""
def reverse_in_place(list):
    left_index = 0
    right_index = len(list) -1

    while left_index < right_index:
        list[left_index] = list[right_index]
        list[right_index] = list[left_index]
        left_index += 1
        right_index -= 1