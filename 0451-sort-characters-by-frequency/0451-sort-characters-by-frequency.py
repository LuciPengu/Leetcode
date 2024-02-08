class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        s = sorted(s)
        s = sorted(s, key= lambda x: count[x], reverse=True)
        return s