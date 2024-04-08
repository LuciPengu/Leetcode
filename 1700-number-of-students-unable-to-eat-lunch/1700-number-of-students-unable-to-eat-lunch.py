class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        square = students.count(1)
        circle = students.count(0)
        
        while sandwiches:
            print(sandwiches)
            
            if sandwiches[0] == 1 and square > 0:
                square -= 1
                sandwiches.pop(0)
            elif sandwiches[0] == 0 and circle > 0:
                circle -= 1
                sandwiches.pop(0)
            
            else:
                return circle+square
        
        return 0