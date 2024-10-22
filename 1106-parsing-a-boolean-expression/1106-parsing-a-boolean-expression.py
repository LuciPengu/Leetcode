class Solution:
    def parseBoolExpr(self, exp: str) -> bool:
        
        
        for i in range(len(exp)-1,0,-1):
            if exp[i] == "(":
                j = i+1
                evaluate = ""
                expression = exp[i-1]
                while exp[j] != ")":
                    evaluate += exp[j]
                    j+=1
                
                newVal = ""
                if expression == "!":
                    newVal = "t" if evaluate == "f" else "f"
                
                elif expression == "|":
                    newVal = "t" if "t" in evaluate.split(",") else "f"
                    print(newVal)
                else:
                    newVal = "t" if len(set(evaluate.split(","))) == 1 and evaluate.split(",")[0] == "t" else "f"
                    print(newVal)
                    
                exp = exp[0:i-1] + newVal + exp[j+1:]
        
        return True if exp == "t" else False
                