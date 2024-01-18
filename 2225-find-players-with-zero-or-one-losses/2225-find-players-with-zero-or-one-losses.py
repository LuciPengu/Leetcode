class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = defaultdict(int)
        losses = defaultdict(int)
        for win, lose in matches:
            losses[lose] += 1
            if win not in losses:
                losses[win] = 0
        
        res = [[],[]]
        
        for i in sorted(losses):
            if losses[i] == 0:
                res[0].append(i)
            elif losses[i] == 1:
                res[1].append(i)
        
        return res