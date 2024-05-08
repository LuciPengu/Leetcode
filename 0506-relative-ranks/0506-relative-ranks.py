class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [[i,j] for i,j in enumerate(score)]
        ans = [0]*len(score)
        print(score)
        score.sort(key = lambda x:x[1], reverse=True)
        
        medals = ["Gold Medal","Silver Medal","Bronze Medal"]
        
        i = 1
        for index, value in score:
            if i < len(medals)+1:
                ans[index] = medals[i-1]
            else:
                ans[index] = str(i)
            i+=1
        
        return ans