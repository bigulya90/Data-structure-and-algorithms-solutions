# """
# input: [1-3], [2-4]
# output: [1-4]
#
#
# """
# def merged_meetings(meetings):
#     sorted_meetings = sorted(meetings)
#     merged_meetings = sorted_meetings[0]
#
#     for curr_start, curr_end in sorted_meetings[1:]:
#         last_merged_start, last_merged_end = merged_meetings[-1]
#
#         if curr_start <= last_merged_end:
#             merged_meetings[-1] = last_merged_start, max(last_merged_end, curr_start)
#         else:
#             merged_meetings.append(curr_start, curr_end)
#
#     return merged_meetings()
#
#
# # reverse string in-place
# def reverse_string_inplace(list_of_chars):
#     left_index = 0
#     right_index = len(list_of_chars) - 1
#
#     while left_index < right_index:
#         # Swap characters
#         list_of_chars[left_index], list_of_chars[right_index] = \
#             list_of_chars[right_index], list_of_chars[left_index]
#
#         # Move towards middle
#         left_index += 1
#         right_index -= 1
#     return list_of_chars
#
#
# print (reverse_string_inplace([1, 2, 3, 4, 5]))
#
#
# def find_movies(flight, movies):
#     movies_seen = set()
#
#     for i in movies:
#         second = flight - i
#         if second in movies_seen:
#             return True
#         else:
#             movies_seen.add(i)
#     return False




def ransom_note(magazine, ransom):

    ndict = {}

    for k in magazine:
        if k in ndict.keys():
            ndict[k] += 1
        else:
            ndict[k] = 1

    count = 0
    for item in ransom:
        if item in ndict.keys():
            ndict[item] -= 1
            count += 1
        else:
            break
    return len(ransom) == count

a = "biga"
b = "bi"
print (ransom_note(a, b))




