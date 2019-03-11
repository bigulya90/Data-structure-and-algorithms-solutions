class Intervals(object):
    def __init(self, start = 0, end = 0):
        self.start = start
        self.end = end

class Solution(object):
    def merge_intervals(self, interval_list):

        #sort by start
        interval_list.sort(key=lambda x: x.start)

        merged_list = []

        for interval in interval_list:
            if not merged_list or merged_list[-1].end < interval_list.start:
                merged_list.append(interval)
            else:
                merged_list[-1].end = max(merged_list[-1].end, interval.end)
        return merged_list


