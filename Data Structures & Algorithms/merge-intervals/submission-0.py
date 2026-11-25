class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting + greedy
        # intervals.sort()
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        # go through rest of intervals and check for overlap
        for start, end in intervals[1:]:
            lastEnd= merged[-1][1]

            # [[1,3],[1,5],[6,7]]
            if start <= lastEnd:
                # update the end value of the last interval in merged
                merged[-1][1] = max(lastEnd, end)
            else: 
                # regular append 
                merged.append([start, end])
        
        return merged 


