class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        tval = len(arr)-k
        arr = Counter(arr)
        arr = list(sorted(arr.items(), key=lambda x:x[1]))
        count = 0
        while tval > 0:
            maxi = arr[len(arr) - count - 1][1]
            tval -= maxi
            count += 1  
        return count