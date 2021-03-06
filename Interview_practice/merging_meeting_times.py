# input: [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# output :   [(0, 1), (3, 8), (9, 12)]

"""
1. no overlap (1-3), (2-4)
2. edge cases:

The end time of the first meeting and the start time of the second meeting are equal. For example: [(1, 2), (2, 3)]
The second meeting ends before the first meeting ends. For example: [(1, 5), (2, 3)]
"""

# O(nlgn) time and O(n)O(n) space.

def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings


print (merge_ranges([(1,3),(2,4)]))












































































