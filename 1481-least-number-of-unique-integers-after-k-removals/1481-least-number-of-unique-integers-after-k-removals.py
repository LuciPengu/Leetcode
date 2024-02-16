class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        
        arr = list(set(arr))
        arr.sort(key=lambda x:count[x])
        print(arr)
        for i in arr:
            if k >= count[i]:
                k -= count[i]
                del count[i]
        return len(count.items())