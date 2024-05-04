class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        
        v1 = v1.split(".")
        v2 = v2.split(".")
        v1arr, v2arr = [], []
        for char in v1:
            v1arr.append(int(char))
        for char in v2:
            v2arr.append(int(char))
        
        
        if v1arr == v2arr:
            return 0
        
        
        for i in range(len(v1arr)):
            try:
                if v1arr[i] > v2arr[i]:
                    return 1
                elif v1arr[i] < v2arr[i]:
                    return -1
            except:
                if v1arr[i] > 0:
                    return 1
        
        print(i)
        for j in range(i+1, len(v2arr)):
            if v2arr[j] > 0:
                return -1
        return 0