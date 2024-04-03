class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        sortKey = lambda x: x[2]
        
        posdict = defaultdict(int)
        
        for i in range(len(positions)):
            posdict[positions[i]] = i 
        
        robots = [(x, y, _) for x, y, _ in sorted(zip(directions, healths, positions), key=sortKey)]
        
        stack = []
        escaped = []
        
        for direction, health, pos in robots:
            if direction == "R":
                stack.append([health, pos])
            
            elif direction == "L":

                while stack and health > stack[-1][0]:
                    stack.pop()
                    health -= 1

                if stack and health < stack[-1][0]:
                    stack[-1][0] -= 1
                    continue
                
                if stack and health == stack[-1][0]:
                    stack.pop()
                    continue
                    
                if health > 0:
                    escaped.append((health, pos))
        
        return [i for i, j in sorted(escaped + stack, key=lambda x:posdict[x[1]])]