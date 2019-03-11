# a = [1, 3, 5]
# b = [2, 4, 6]
# result = [1, 2, 3, 4, 5, 6]


# find the smallest first index
def merge(first, second):
    merged_list_size = len(first) + len(second)
    merged_list = [None] * merged_list_size  # Whyyyyyyy?

    head_first = first[0]
    head_second = second[0]

    if head_first < head_second:
        merged_list[0] = head_first
    else:
        merged_list[0] = head_second

    return merged_list


def merge_lists(my_list, alices_list):
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:
        first_unmerged_alices = alices_list[current_index_alices]
        first_unmerged_mine = my_list[current_index_mine]

        if first_unmerged_mine < first_unmerged_alices:
            # Case: next comes from my list
            merged_list[current_index_merged] = first_unmerged_mine
            current_index_mine += 1
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = first_unmerged_alices
            current_index_alices += 1

        current_index_merged += 1

    return merged_list









