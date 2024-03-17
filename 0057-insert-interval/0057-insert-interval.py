class Solution:
    def insert(self, inte: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        inte.append(newInterval)
        inte.sort(key=lambda x: x[0])
        n = len(inte)
        res = []
        i = 0
        while i < n:
            temp = inte[i]
            print(temp)
            i+=1
            while i < n:
                print(temp, inte[i])
                if temp[1] >= inte[i][0]:
                    temp = [temp[0],max(temp[1],inte[i][1])]
                    i+=1
                else:
                    break
            res.append(temp)
            
                
        return(res)
        
                
            