class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        
        curr = 0
        mul = 1
        res = 0
        for key, val in count.most_common():
            print(key, val)
            if curr % 8 == 0 and curr != 0:
                mul += 1
            
            curr += 1
            res += val * mul
        return res