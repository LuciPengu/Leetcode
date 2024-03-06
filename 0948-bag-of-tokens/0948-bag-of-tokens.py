class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        if tokens == []:
            return 0
        while(len(tokens) > 0 and power >= tokens[0]):
            power -= tokens.pop(0)
            score += 1
            if len(tokens) >= 2 and power < tokens[0]:
                power += tokens.pop(-1)
                score -= 1
        return score