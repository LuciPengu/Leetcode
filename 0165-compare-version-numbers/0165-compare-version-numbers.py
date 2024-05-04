class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        
        v1 = v1.split(".")
        v2 = v2.split(".")
        n = max(len(v1), len(v2))
        
        v2 = v2 + ["0"]*(n-len(v2))
        v1 = v1 + ["0"]*(n-len(v1))
        

        for i in range(n):            
            if int(v2[i]) < int(v1[i]):
                return 1
            elif int(v2[i]) > int(v1[i]):
                return -1
        return 0