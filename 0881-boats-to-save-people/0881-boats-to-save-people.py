class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        l, r = 0, len(people)-1
        
        boat = 0
        boats = 0
        boatlen = 0
        while l <= r:
            if boat + people[r] <= limit and boatlen < 2:
                boat += people[r]
                r -= 1
                boatlen += 1
            
            elif boat + people[l] <= limit and boatlen < 2:
                boat += people[l]
                l += 1
                boatlen += 1
                
            else:
                boat = 0
                boats += 1
                boatlen = 0
        
        print(boat)
        if boat > 0:
            return boats+1
        return boats