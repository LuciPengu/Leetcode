from typing import List
from functools import lru_cache

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Possible knight moves
        moves = [
            (2,1), (2,-1), (-2,1), (-2,-1),
            (1,2), (1,-2), (-1,2), (-1,-2)
        ]
        
        @lru_cache(None)
        def dp(x: int, y: int, remaining: int) -> float:
            # Base case: out of board
            if x < 0 or x >= n or y < 0 or y >= n:
                return 0
            
            # No more moves left, still on board
            if remaining == 0:
                return 1
            
            # Calculate probability of staying on board
            prob = 0
            for dx, dy in moves:
                prob += 0.125 * dp(x + dx, y + dy, remaining - 1)
            
            return prob
        
        return dp(row, column, k)