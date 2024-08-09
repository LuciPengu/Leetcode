class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, x: int, y: int) -> List[List[int]]:
        matrix = [[0 for i in range(cols)] for i in range(rows)]
        
        go = 0
        mode = 0
        soln = []
        added = 0
        while added < rows * cols:
            if mode == 0:
                go += 1
                for i in range(go):
                    if x in range(rows) and y in range(cols):
                        soln.append([x,y])
                        added += 1
                    y += 1
                mode += 1
            
            if mode == 1:
                for i in range(go):
                    if x in range(rows) and y in range(cols):
                        soln.append([x,y])
                        added += 1
                    x += 1
                mode += 1
            if mode == 2:
                go += 1
                for i in range(go):
                    if x in range(rows) and y in range(cols):
                        soln.append([x,y])
                        added += 1
                    y -= 1
                mode += 1
            if mode == 3:
                for i in range(go):
                    if x in range(rows) and y in range(cols):
                        soln.append([x,y])
                        added += 1
                    x -= 1
                mode = 0
        return soln