class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        res = [-1,-1]
        i = 0
        for start, end in points:
            rs, re = res
            if re >= start >= rs or re >= end >= rs:
                res = [max(rs, start), min(end, re)]
            else:
                res = [start,end]
                i+=1
        return i