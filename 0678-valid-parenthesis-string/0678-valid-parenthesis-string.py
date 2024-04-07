class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        empty = []
        res = ""
        
        for i, char in enumerate(s):                
            
            if char == ")":
                if stack:
                    stack.pop(-1)
                elif empty:
                    empty.pop(-1)
                else:
                    return False
                
            elif char == "(":
                stack.append(i)
            
            else:
                empty.append(i)
        
        
        print(stack, empty)    
        l = 0
        removed = []
        
        if len(empty) < len(stack):
            return False
        
        for r in range(len(stack)):
            try:
                while empty[l] < stack[r]:
                    l+=1
                if empty[l] > stack[r]:
                    print(empty[l], stack[r])
                    empty.pop(l)
                    removed.append(stack[r])
            except:
                return False
        
        return removed == stack
            
            
                