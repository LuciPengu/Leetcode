class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        res = [[-1,-1]]
        for start, end in points:
            rs, re = res[-1]
            if re >= start >= rs or re >= end >= rs:
                res[-1] = [max(rs, start), min(end, re)]
            else:
                res.append([start,end])
        return len(res)-1